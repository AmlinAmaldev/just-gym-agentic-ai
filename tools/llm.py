from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",   # FASTEST
    temperature=0.2,           # faster + deterministic
    max_output_tokens=300      # limit output
)
