# Cloud FinOps Cost Optimization & Anomaly Detection Engine

## Overview
Python-based cloud cost intelligence system detecting anomalies, forecasting spend, and generating optimization recommendations.

## Tech Stack
- Python
- Pandas
- NumPy
- Scikit-Learn
- FastAPI
- Streamlit
- Docker

## Setup
pip install -r requirements.txt
python -m uvicorn app.api:app --reload
streamlit run dashboard/dashboard.py