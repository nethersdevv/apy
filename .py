from fastapi import FastAPI
import os
import time

app = FastAPI(title="Brainrot API")

@app.get("/")
async def home():
    return {"status": "✅ API OK", "port": os.getenv("PORT", "8000")}

@app.get("/recent")
async def get_recent(limit: int = 60):
    return {
        "ok": True,
        "findings": [],
        "last_update": int(time.time())
    }

print("🚀 Brainrot API démarrée avec succès sur Railway")
