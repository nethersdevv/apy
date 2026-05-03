from fastapi import FastAPI
import time

app = FastAPI(title="Brainrot API")

@app.get("/")
async def home():
    return {"status": "OK", "message": "API en ligne"}

@app.get("/recent")
async def get_recent():
    return {
        "ok": True,
        "findings": [],
        "last_update": int(time.time())
    }

print("🚀 API démarrée avec succès")
