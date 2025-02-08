from fastapi import FastAPI
import pickle
from schemas import (
    Features,
    PredictResponse,
    preprocess_input
)

app = FastAPI(title='Predict Churn')

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.post('/predict/', response_model=PredictResponse)
def predict(features: Features):
    input_data = preprocess_input(features)

    prediction = model.predict(input_data)

    return {"churn": int(prediction[0])}