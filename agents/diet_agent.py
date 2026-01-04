from tools.llm import llm

def generate_diet(profile):
    prompt = f"""
    Create a healthy diet plan based on:
    Age: {profile['age']}
    Weight: {profile['weight']}
    Height: {profile['height']}
    Workout type: {profile['workout_type']}
    Any medical condition: {profile['medication']}
    """
    return llm.invoke(prompt).content
