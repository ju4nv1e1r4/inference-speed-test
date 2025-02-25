from pydantic import BaseModel
import numpy as np

# Features
FEATURE_COLUMNS = [
    "Gender_Female", "Gender_Male",
    "Subscription Type_Basic", "Subscription Type_Premium", "Subscription Type_Standard",
    "Contract Length_Annual", "Contract Length_Monthly", "Contract Length_Quarterly"
]

# Map das Features
GENDER_MAP = {"Female": [1, 0], "Male": [0, 1]}
SUBSCRIPTION_MAP = {
    "Basic": [1, 0, 0],
    "Premium": [0, 1, 0],
    "Standard": [0, 0, 1]
}
CONTRACT_MAP = {
    "Annual": [1, 0, 0],
    "Monthly": [0, 1, 0],
    "Quarterly": [0, 0, 1]
}

# BaseModels Pydantic 
class Features(BaseModel):
    gender: str
    subscription_type: str
    contract_length: str

class PredictResponse(BaseModel):
    churn: int

# Pré-processamento dos inputs
def preprocess_input(features: Features):
    gender = GENDER_MAP.get(features.gender, [0, 0])  # Se não encontrar, assume [0, 0]
    subscription = SUBSCRIPTION_MAP.get(features.subscription_type, [0, 0, 0])
    contract = CONTRACT_MAP.get(features.contract_length, [0, 0, 0])
    
    input_vector = gender + subscription + contract

    return np.array([input_vector])
