# House Price Prediction — Student Project

A student project implementing a house price prediction web application with:
- FastAPI backend for prediction API.
- React + TypeScript frontend built with Vite.
- Model pipeline using scikit-learn and joblib.

## Architecture

```
User Browser
   │
   │  HTTP POST /api/predict
   ▼
Frontend (Vite React)
   │
   │  HTTP JSON request
   ▼
Backend (FastAPI)
   │
   │  preprocess request → model.predict
   ▼
Model pipeline (joblib, pandas)
   │
   ▼
Response JSON
```

## Tech stack

- Python 3.11+
- FastAPI
- Uvicorn
- Pydantic
- pandas
- scikit-learn
- joblib
- pytest
- React
- TypeScript
- Vite

## Project structure

- `backend/` — FastAPI application and service code.
  - `backend/main.py` — app entrypoint, CORS, lifespan, routes.
  - `backend/app/api/routes/prediction_routes.py` — prediction endpoint.
  - `backend/app/schemas/prediction.py` — request/response models.
  - `backend/app/services/` — model loading and preprocessing.
  - `backend/app/models/` — model and reference locations files.
  - `backend/tests/` — backend test cases.
- `frontend/` — React + TypeScript UI.
  - `frontend/src/` — React application code.
  - `frontend/src/api/predictionClient.ts` — API client.
  - `frontend/src/types/prediction.ts` — shared input/output types.
- `notebooks/` — notebook artifacts and local model/export files.
- `requirements.txt` — Python dependencies.
- `.gitignore` — ignored files for Git.
- `README.md` — repository instructions.

## Dataset and model download

- The raw dataset is not included in this repository because it may be too large. Only model artifacts and code are included.
- If you have a dataset CSV, place it locally and use the notebook or training script to reproduce the model.
- The trained model file `backend/app/models/house_price_rf_model.pkl` is also excluded from Git because it exceeds 50MB.
- Download the model file from instructor-provided storage or GitHub Release, then place it at:
  - `backend/app/models/house_price_rf_model.pkl`

## Backend setup

```powershell
cd C:\Users\HP\house-price-project
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn backend.main:app --reload --port 8000
```

## Frontend setup

```bash
cd frontend
npm install
npm run dev
```

Then open:
- `http://localhost:5173`

## Environment variables

| File | Variable | Purpose |
| --- | --- | --- |
| `frontend/.env.example` | `VITE_API_BASE_URL` | Backend API base URL for the frontend |
| `backend/.env.example` | `MODEL_PATH` (optional) | Overrides the model file path if used |

Copy examples:

```bash
cp frontend/.env.example frontend/.env
cp backend/.env.example backend/.env
```

## API reference

### POST /api/predict

Request body matches `frontend/src/types/prediction.ts`:
- `location`: string
- `carpet_area_sqft`: number
- `floor_num`: number
- `bathroom`: number
- `balcony`: number
- `furnishing`: `Furnished` | `Semi-Furnished` | `Unfurnished`
- `transaction`: `New Property` | `Resale`
- `ownership`: string
- `facing`: string

Response:

```json
{
  "status": "ok",
  "predicted_price": 1234567.0
}
```

Example curl:

```bash
curl -X POST http://localhost:8000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"location":"mumbai","carpet_area_sqft":1200.0,"floor_num":5,"bathroom":2,"balcony":1,"furnishing":"Semi-Furnished","transaction":"Resale","ownership":"Freehold","facing":"East"}'
```

## Tests

Run backend tests from the repository root:

```bash
pytest -q
```

## Model metrics

Model metrics are not included in this repository because the raw dataset is not provided here. Compute and record metrics such as MAE, RMSE, and R² after evaluating the model with the dataset.

## Screenshots

Add screenshots of the running app in a `screenshots/` folder if required for submission.

## Submission checklist

- [x] `.gitignore` exists and excludes `.venv/`, `__pycache__/`, `node_modules/`, `dist/`, `.env`, `*.log`, and large raw datasets.
- [x] Repository initialized with Git and committed.
- [x] Root `README.md` includes overview, stack, structure, setup, env, API, model/dataset instructions.
- [x] Backend and frontend setup commands are present.
- [x] Large `.pkl` model and raw dataset files are excluded from Git.
- [x] Backend tests pass.
