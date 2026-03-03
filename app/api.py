from fastapi import FastAPI
from .ingestion import load_data
from .preprocessing import preprocess
from .anomaly_detection import detect_anomalies
from .forecasting import forecast_cost
from .optimization import optimization_recommendations

app = FastAPI()

@app.get("/analysis")
def run_analysis():
    df = load_data("../data/sample_billing.csv")
    df = preprocess(df)
    df = detect_anomalies(df)

    forecast = forecast_cost(df)
    recommendations = optimization_recommendations(df)

    return {
        "anomalies": df[df['anomaly']==1].to_dict(orient="records"),
        "forecast": forecast,
        "recommendations": recommendations
    }