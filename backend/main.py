
from pathlib import Path

import joblib
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="SMS Shield API",
    description="SMS Spam Detection Backend",
    version="1.0.0"
)

# Allow Streamlit to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict this in production
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model location
MODEL_PATH = Path(__file__).parent / "model" / "sms_spam_model.joblib"

model = None


@app.on_event("startup")
def load_model():
    global model

    if MODEL_PATH.exists():
        model = joblib.load(MODEL_PATH)
        print("ML model loaded successfully!")
    else:
        print("Model not found. Waiting for Member 2 to provide it.")


# Request schema
class SMSRequest(BaseModel):
    message: str


# Root endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to SMS Shield API",
        "status": "running"
    }


# Health check
@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": model is not None
    }


# SMS prediction endpoint
@app.post("/predict")
def predict_sms(request: SMSRequest):

    if not request.message.strip():
        raise HTTPException(
            status_code=400,
            detail="SMS message cannot be empty"
        )

    if model is None:
        raise HTTPException(
            status_code=503,
            detail="ML model is not available yet"
        )

    prediction = model.predict([request.message])[0]

    return {
        "message": request.message,
        "prediction": str(prediction),
        "result": "Spam" if prediction.lower() == "spam" else "Not Spam"
    }
