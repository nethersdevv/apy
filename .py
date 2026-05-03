from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/")
def home():
    return {"status": "API OK - Test minimal"}

@app.get("/recent")
def recent():
    return {"ok": True, "findings": [], "last_update": int(time.time())}

print("✅ API minimale démarrée")
