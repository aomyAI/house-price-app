from typing import Literal

from pydantic import BaseModel


class PredictionRequest(BaseModel):
    location: str
    carpet_area_sqft: float
    floor_num: int
    bathroom: int
    balcony: int
    furnishing: Literal["Furnished", "Semi-Furnished", "Unfurnished"]
    transaction: Literal["New Property", "Resale"]
    ownership: str
    facing: str


class PredictionResponse(BaseModel):
    status: Literal["ok"] = "ok"
    predicted_price: float
