from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Review(BaseModel):
    review_text: str

@app.get("/")
def root():
    return {"message": "API is working"}

@app.post("/predict")
def predict_rating(review: Review):
    length = len(review.review_text)
    score = min(10, max(0, length // 10))  # 단순한 예측 로직
    return {"predicted_score": score}
