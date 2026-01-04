from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from starlette.concurrency import run_in_threadpool
from agents.orchestrator_agent import handle_profile

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def ui():
    return open("ui/index.html", encoding="utf-8").read()

@app.post("/submit")
async def submit(profile: dict):
    try:
        reply = await run_in_threadpool(handle_profile, profile)
        return {"reply": reply}   # ✅ ALWAYS JSON
    except Exception as e:
        print("🔥 BACKEND ERROR:", e)   # VERY IMPORTANT
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}   # ✅ STILL JSON
        )
