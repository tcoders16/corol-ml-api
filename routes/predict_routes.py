from fastapi import APIRouter
from controller.predict_controller import predict

router = APIRouter()

router.post("/predict")(predict)