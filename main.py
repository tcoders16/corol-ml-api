from dotenv import load_dotenv
load_dotenv()



from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.predict_routes import router as PredictRouter
import uvicorn
from routes.auth_routes import router as AuthRouter


app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],

    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# register routes
app.include_router(AuthRouter, prefix="/api/auth")
app.include_router(PredictRouter, prefix="/api")


@app.get("/")
def root():
    return {"message": "FastAPI backend is running!"} 

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)