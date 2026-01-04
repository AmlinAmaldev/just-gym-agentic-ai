from tools.llm import llm

def improve(analysis):
    prompt = f"Suggest improvements based on: {analysis}"
    return llm.invoke(prompt).content
