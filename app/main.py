import logging
import time

from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline


# --------------------------------------------------
# Logging
# --------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


# --------------------------------------------------
# Model
# --------------------------------------------------

MODEL_NAME = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"

logger.info("Loading model: %s", MODEL_NAME)

classifier = pipeline(
    "sentiment-analysis",
    model=MODEL_NAME
)

logger.info("Model loaded successfully")


# --------------------------------------------------
# FastAPI
# --------------------------------------------------

app = FastAPI(
    title="Sentiment Analysis API",
    version="1.0.0"
)


# --------------------------------------------------
# Request model
# --------------------------------------------------

class PredictionRequest(BaseModel):
    text: str


# --------------------------------------------------
# Health endpoint
# --------------------------------------------------

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model": MODEL_NAME
    }


# --------------------------------------------------
# Prediction endpoint
# --------------------------------------------------

@app.post("/predict")
def predict(request: PredictionRequest):

    start_time = time.time()

    result = classifier(request.text)[0]

    latency = time.time() - start_time

    logger.info(
        "prediction | text_length=%d | label=%s | latency_ms=%.2f",
        len(request.text),
        result["label"],
        latency * 1000
    )

    return {
        "text": request.text,
        "label": result["label"],
        "score": result["score"],
        "latency_ms": round(latency * 1000, 2)
    }