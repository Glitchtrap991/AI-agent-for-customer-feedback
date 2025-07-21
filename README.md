# 🧠 AI Customer Feedback Analyzer (Hackathon Project)

This is an AI Agent that ingests customer feedback from CSV files, performs sentiment and keyword analysis, recommends product feature improvements, and sends insights via Slack using the Gemini API.

## 🚀 Demo
🌐 Live App: [https://your-streamlit-app.streamlit.app](https://your-streamlit-app.streamlit.app)

## 📦 Features
- Upload customer feedback CSV files
- Real-time sentiment & keyword extraction
- Slack alert system for negative/high-priority feedback
- Gemini AI integration for insight & feature generation
- Query-handling chatbot interface

## 🛠️ Tech Stack
- **Frontend**: Streamlit
- **Backend**: Python
- **LLM**: Gemini API
- **Notification**: Slack Webhooks
- **Hosting**: Streamlit Cloud

## 📁 How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```
---
2. Install dependencies:
```bash
pip install -r requirements.txt
```
---

3. (Optional) Create .streamlit/secrets.toml for API keys:

toml
Copy
Edit
[credentials]
gemini_api_key = "your_api_key"
slack_webhook_url = "your_webhook_url"
Run the app:

bash
Copy
Edit
streamlit run app.py

---

4. 📝 Sample Input Format
Upload a CSV file with the following structure:

id	feedback
1	The product packaging was poor.

---

5. 📹 Submission Video (3 mins)
🎥 [Watch Demo Video](https://www.youtube.com/watch?v=dQw4w9WgXcQ](https://youtu.be/8pSmz6AvHS8))

---
