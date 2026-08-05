import json
import os

import pandas as pd


LOCATIONS_PATH = os.path.join(os.path.dirname(__file__), "../models/locations.json")


def load_locations():
    with open(LOCATIONS_PATH, encoding="utf-8") as f:
        return {loc.lower() for loc in json.load(f)}


KNOWN_LOCATIONS = load_locations()


def normalize_location(location: str) -> str:
    location_normalized = location.strip().lower()
    if location_normalized in KNOWN_LOCATIONS:
        return location_normalized
    return "other"


def preprocess_request(data):
    return pd.DataFrame([
        {
            "carpet_area_sqft": data.carpet_area_sqft,
            "floor_num": data.floor_num,
            "bathroom": data.bathroom,
            "balcony": data.balcony,
            "location_grouped": normalize_location(data.location),
            "Furnishing": data.furnishing,
            "Transaction": data.transaction,
            "Ownership": data.ownership,
            "facing": data.facing,
        }
    ])
