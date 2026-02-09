from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.schemas import Details
from app.services.inference import predict_survival

router = APIRouter()

@router.post("/predict")
def predict(details: Details):
    result = predict_survival(details)
    return JSONResponse(
        status_code=200,
        content={"cancer_prediction": result}
    )
