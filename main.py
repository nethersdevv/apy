from fastapi import FastAPI
import os
import time

app = FastAPI(title="Brainrot API")

@app.get("/")
async def home():
    return {"status": "✅ API OK"}

@app.get("/recent")
async def get_recent():
    return {
        "ok": True,
        "findings": [],
        "last_update": int(time.time())
    }

print("🚀 API démarrée")
