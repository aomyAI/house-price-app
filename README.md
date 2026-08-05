# House Price Prediction — Student Project

This repository contains a FastAPI backend and a React + TypeScript (Vite) frontend for predicting house prices.

Quick status
- Backend: FastAPI app listening on `http://localhost:8000` (see `backend/main.py`).
- Frontend: Vite dev server on `http://localhost:5173` (see `frontend/`).

Requirements
- Python 3.11+ and Node.js 18+.

Setup (backend)

```powershell
# create and activate venv (Windows PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn backend.main:app --reload --port 8000
```

Setup (frontend)

```bash
cd frontend
npm install
npm run dev
# open http://localhost:5173
```

Environment
- Copy `frontend/.env.example` -> `frontend/.env` and update `VITE_API_BASE_URL` if needed.
- `backend/.env.example` is provided as a reference.

Model file
- The model used by the backend is expected at `backend/app/models/house_price_rf_model.pkl`.
- This repository does not include the `.pkl` model file because it exceeds 50MB.
- Upload the model file to a cloud storage service or GitHub Release, then download it manually and place it at `backend/app/models/house_price_rf_model.pkl`.
- Example: `backend/app/models/house_price_rf_model.pkl`

API
- POST `/api/predict` — accepts a JSON matching `frontend/src/types/prediction.ts` and returns `{status: "ok", predicted_price: number}`.

Tests
- Run `pytest` from the repository root. The project includes simple backend tests.

Git / Submission checklist
- Add `.gitignore` (present).
- Remove raw datasets from the repo (large CSVs). Keep dataset references in the README.
- If you host the model externally, include download instructions here.

Example curl

```bash
curl -X POST http://localhost:8000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"location":"mumbai","carpet_area_sqft":1200.0,"floor_num":5,"bathroom":2,"balcony":1,"furnishing":"Semi-Furnished","transaction":"Resale","ownership":"Freehold","facing":"East"}'
```
