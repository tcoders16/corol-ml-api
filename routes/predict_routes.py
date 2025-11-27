from fastapi import APIRouter, Header
from fastapi import  HTTPException
import jwt
import os
from controller.predict_controller import predict


router = APIRouter()

JWT_SECRET = os.getenv("JWT_SECRET")

def verify_token(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing token")

    token = authorization.replace("Bearer ", "")

    try:
        decoded = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return decoded  
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

router.post("/predict")(predict)