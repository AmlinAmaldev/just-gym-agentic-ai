from tools.llm import llm

def plan_workout(profile):
    prompt = f"""
    Create a {profile['workout_type']} workout plan.
    Goal: fitness
    Age: {profile['age']}
    Weight: {profile['weight']}
    Keep it concise.
    """
    return llm.invoke(prompt).content

