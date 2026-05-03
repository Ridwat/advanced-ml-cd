from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import time

app = FastAPI(title="ONNX Sentiment Analysis API")

class TextInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "ONNX Sentiment Analysis API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/predict")
def predict_sentiment(input_data: TextInput):
    text = input_data.text.strip()

    if not text:
        raise HTTPException(status_code=400, detail="Input text cannot be empty")

    if len(text) > 1000:
        raise HTTPException(status_code=400, detail="Input text is too long")

    positive_words = ["good", "great", "excellent", "happy", "love", "amazing"]
    negative_words = ["bad", "terrible", "sad", "hate", "poor", "awful"]

    lower_text = text.lower()

    if any(word in lower_text for word in positive_words):
        sentiment = "positive"
    elif any(word in lower_text for word in negative_words):
        sentiment = "negative"
    else:
        sentiment = "neutral"

    processing_time = round(time.time(), 4)

    return {
        "input": text,
        "sentiment": sentiment,
        "processing_time": processing_time
    }