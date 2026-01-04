from tools.llm import llm
from agents.memory_agent import read_memory

def analyze():
    memory = read_memory()
    prompt = f"Analyze this workout history: {memory}"
    return llm.invoke(prompt).content
