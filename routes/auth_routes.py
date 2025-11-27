from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
import jwt
import datetime

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

JWT_SECRET = os.getenv("JWT_SECRET")


USERS = [
    {
        "username": os.getenv("ADMIN_1_USERNAME"),
        "password": os.getenv("ADMIN_1_PASSWORD")
    },
    {
        "username": os.getenv("ADMIN_2_USERNAME"),
        "password": os.getenv("ADMIN_2_PASSWORD")
    }
]
print("Loaded users:", USERS)

@router.post("/auth/login")
def login(req: LoginRequest):
    for user in USERS:
        if user["username"] == req.username and user["password"] == req.password:
            token = jwt.encode(
                {
                    "username": req.username,
                    "role": "admin",
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=12),
                },
                JWT_SECRET,
                algorithm="HS256"
            )
            return {"token": token}

    raise HTTPException(status_code=401, detail="Invalid username or password")