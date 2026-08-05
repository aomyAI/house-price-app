import joblib
import os

from backend.app.services.preprocessing import preprocess_request

MODEL_PATH = os.path.join(os.path.dirname(__file__), "../models/house_price_rf_model.pkl")

model = None


def load_model():
    global model
    if model is not None:
        return model

    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

    model = joblib.load(MODEL_PATH)
    return model


def get_prediction(data):
    global model
    if model is None:
        load_model()

    input_data = preprocess_request(data)
    prediction = model.predict(input_data)
    return float(prediction[0])
