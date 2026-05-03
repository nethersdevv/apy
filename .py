from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
import time
import os

app = FastAPI(title="Brainrot API")

class Pet(BaseModel):
    id: int
    name: str
    base_name: str
    value: int
    mutation: Optional[str] = None
    tier: str = "Midlights"
    timestamp: int
    job_id: Optional[str] = None

logs: List[dict] = []

@app.get("/recent")
async def get_recent(limit: int = 60):
    sorted_logs = sorted(logs, key=lambda x: x.get("timestamp", 0), reverse=True)[:limit]
    return {
        "ok": True,
        "findings": sorted_logs,
        "last_update": int(time.time())
    }

@app.post("/add")
async def add_pet(pet: Pet):
    # Évite les doublons
    if not any(x.get("id") == pet.id for x in logs):
        logs.append(pet.dict())
        print(f"✅ Ajouté : {pet.name} | {pet.value:,} | {pet.tier}")
    return {"ok": True, "message": "Pet ajouté"}

@app.get("/")
async def home():
    return {
        "status": "OK",
        "total_logs": len(logs),
        "port": os.getenv("PORT", "8000")
    }

print("🚀 API Brainrot démarrée !")
