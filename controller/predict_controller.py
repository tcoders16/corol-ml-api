from fastapi import HTTPException
from models.strength_input import StrengthInput
from services.ml_service import predict_strength

def predict(data: StrengthInput):
    try:
        return predict_strength(data)
    
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))