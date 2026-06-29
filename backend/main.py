from fastapi import FastAPI
from backend.predict import router as predict_router

app = FastAPI(
    title="CyberPulse AI",
    description="AI-Powered Network Intrusion Detection System",
    version="1.0"
)

app.include_router(predict_router)

@app.get("/")
def home():
    return {
        "project": "CyberPulse AI",
        "version": "1.0",
        "status": "Running",
        "developer": "SKARD",
        "message": "Welcome to CyberPulse AI 🚀"
    }