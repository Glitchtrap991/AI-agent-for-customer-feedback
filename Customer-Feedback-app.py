import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from textblob import TextBlob
import requests
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Get keys securely
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

if not GEMINI_API_KEY or not SLACK_WEBHOOK_URL:
    st.error("❌ Gemini API key or Slack webhook URL not found. Please configure `.env` or Streamlit secrets.")
    st.stop()

# Configure Gemini client
genai.configure(api_key=GEMINI_API_KEY)

# Function to analyze sentiment
def analyze_sentiments(feedbacks):
    sentiments = [TextBlob(text).sentiment.polarity for text in feedbacks]
    return ["Positive" if s > 0 else "Negative" if s < 0 else "Neutral" for s in sentiments]

# Function to extract keywords
def extract_keywords(feedbacks):
    all_words = " ".join(feedbacks).lower().split()
    filtered = [word for word in all_words if len(word) > 3]
    return Counter(filtered).most_common(10)

# Get Gemini suggestions
def get_gemini_suggestions(feedbacks):
    model = genai.GenerativeModel("gemini-1.5-flash")  # use flash or gemini-pro if you have access
    prompt = f"""You are an AI product expert. Analyze the following customer feedbacks and suggest actionable product features or improvements:

Feedbacks:
{feedbacks}

Give your suggestions in bullet points."""
    response = model.generate_content(prompt)
    return response.text.strip()

# Send to Slack
def send_to_slack(summary):
    payload = {"text": f"📢 *Customer Feedback Summary*\n{summary}"}
    res = requests.post(SLACK_WEBHOOK_URL, json=payload)
    return res.status_code == 200

# Streamlit UI
st.title("💬 Customer Feedback Analyzer")

uploaded_file = st.file_uploader("📂 Upload a CSV file with a 'feedback' column", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    if 'feedback' not in df.columns:
        st.error("❌ 'feedback' column not found in CSV.")
    else:
        feedbacks = df['feedback'].dropna().astype(str).tolist()
        st.success("✅ File uploaded successfully!")

        st.subheader("📊 Sentiment Analysis")
        sentiment_labels = analyze_sentiments(feedbacks)
        st.bar_chart(pd.Series(sentiment_labels).value_counts())

        st.subheader("🔑 Top Keywords")
        for word, count in extract_keywords(feedbacks):
            st.markdown(f"- **{word}**: {count} times")

        if st.button("✨ Generate Feature Suggestions & Send to Slack"):
            with st.spinner("Calling Gemini..."):
                try:
                    suggestions = get_gemini_suggestions(feedbacks[:20])
                    st.subheader("📌 Gemini Suggestions")
                    st.markdown(suggestions)
                    if send_to_slack(suggestions):
                        st.success("✅ Sent to Slack!")
                    else:
                        st.error("❌ Slack sending failed.")
                except Exception as e:
                    st.error(f"Error: {e}")