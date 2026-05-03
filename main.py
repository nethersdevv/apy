from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
import time

app = FastAPI(title="Mon API Brainrot")

logs: List[dict] = []

class Pet(BaseModel):
    id: int
    name: str
    base_name: str
    value: int
    mutation: Optional[str] = None
    tier: str = "Midlights"
    timestamp: int
    job_id: Optional[str] = None

@app.get("/recent")
async def get_recent(limit: int = 60, min_value: int = 10000000):  # 10M par défaut
    # Filtre les pets > 10M
    filtered = [pet for pet in logs if pet.get("value", 0) >= min_value]
    
    sorted_logs = sorted(filtered, key=lambda x: x.get("timestamp", 0), reverse=True)
    return {
        "ok": True,
        "findings": sorted_logs[:limit]
    }

@app.post("/add")
async def add_pet(pet: Pet):
    if not any(x.get("id") == pet.id for x in logs):
        logs.append(pet.dict())
        print(f"✅ Ajouté : {pet.name} | {pet.value:,} | {pet.tier}")
    return {"ok": True}

@app.get("/")
async def home():
    return {"status": "OK", "total": len(logs)}
