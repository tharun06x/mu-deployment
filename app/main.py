from fastapi import FastAPI
from app.routers import prediction

app=FastAPI(title="Cancer Prediction")
app.include_router(prediction.router)

@app.get("/")
def root():
    return{'status':"Cancer Prediction API Running"}