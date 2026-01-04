from agents.cache import get_cache, set_cache
from agents.diet_agent import generate_diet
from agents.workout_agent import plan_workout

def handle_profile(profile):
    key = f"{profile['age']}_{profile['weight']}_{profile['workout_type']}_{profile['diet_required']}"

    cached = get_cache(key)
    if cached:
        return cached

    response = "🏋️ JUST GYM PLAN\n\n"
    response += plan_workout(profile)

    if profile["diet_required"]:
        response += "\n\n🥗 DIET PLAN\n"
        response += generate_diet(profile)

    set_cache(key, response)
    return response
