from fastapi import APIRouter

router = APIRouter()

@router.get("/predict")
def predict():
    return {
        "Prediction": "Port Scan",
        "Severity": "High",
        "Confidence": "97%",
        "Status": "Threat Detected"
    }