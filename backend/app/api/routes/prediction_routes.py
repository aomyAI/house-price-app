from fastapi import APIRouter, HTTPException

from backend.app.schemas.prediction import PredictionRequest, PredictionResponse
from backend.app.services.prediction_service import get_prediction

router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
def predict_house_price(request: PredictionRequest):
    try:
        predicted_price = get_prediction(request)
        return PredictionResponse(predicted_price=predicted_price)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
