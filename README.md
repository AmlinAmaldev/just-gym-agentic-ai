# 🏋️ Just Gym – Agentic AI Fitness Coach

Just Gym is a **browser-based Agentic AI fitness application** that provides
personalized workout and diet plans using **multiple AI agents**.

## 🚀 Features
- 🧠 Multi-agent AI architecture
- 🏋️ Personalized workout plans (Gym / Home)
- 🥗 Optional AI-generated diet plans
- 🛡️ Medical-awareness agent
- ⚡ Fast responses with caching
- 🎨 Animated, modern UI
- 🌐 Web-based chat-style interaction

## 🧩 Agent Architecture
- Orchestrator Agent
- Workout Planning Agent
- Diet Recommendation Agent
- Medical Safety Agent
- Memory & Caching Layer

## 🛠 Tech Stack
- **Backend**: FastAPI
- **AI Models**: Google Gemini
- **Search Tool**: Tavily
- **Frontend**: HTML, CSS, JavaScript
- **Architecture**: Agentic AI (LangChain)

## ▶️ How to Run Locally
```bash
git clone https://github.com/YOUR_USERNAME/just-gym-agentic-ai.git
cd just-gym-agentic-ai
python -m venv venv
source venv/Scripts/activate   # Windows Git Bash
pip install -r requirements.txt
uvicorn main:app --reload
