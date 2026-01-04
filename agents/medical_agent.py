from tools.llm import llm

def check_safety(profile):
    if profile["medication"].lower() == "no":
        return "No medical restrictions."

    prompt = f"""
    The user has the following medical condition:
    {profile['medication']}

    Suggest workout precautions.
    """
    return llm.invoke(prompt).content
