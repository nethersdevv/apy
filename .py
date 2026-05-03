from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import time

app = FastAPI(title="Mon API Brainrot")

logs = []

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
async def get_recent():
    sorted_logs = sorted(logs, key=lambda x: x["timestamp"], reverse=True)[:60]
    return {"ok": True, "findings": sorted_logs}

@app.post("/add")
async def add_pet(pet: Pet):
    if not any(x["id"] == pet.id for x in logs):
        logs.append(pet.dict())
        print(f"✅ Ajouté : {pet.name} | {pet.value:,}")
    return {"ok": True}

@app.get("/")
async def home():
    return {"status": "OK", "total": len(logs)}
