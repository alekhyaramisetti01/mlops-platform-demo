from pathlib import Path
import joblib
from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response


MODEL_PATH = Path("model_artifacts/fraud_model.joblib")

app = FastAPI(title="Fraud Risk Prediction API")


REQUEST_COUNT = Counter("prediction_requests_total",
                        "Total prediction requests")
PREDICTION_LATENCY = Histogram(
    "prediction_latency_seconds", "Prediction latency")


class FraudRequest(BaseModel):
    transaction_amount: float
    account_age_days: float
    num_prev_transactions: float
    avg_transaction_amount: float
    location_risk_score: float
    device_risk_score: float
    merchant_risk_score: float
    payment_velocity: float
    chargeback_history: float
    failed_login_attempts: float


class FraudResponse(BaseModel):
    fraud_prediction: int
    fraud_probability: float


def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError("Model not found. Run training first.")
    return joblib.load(MODEL_PATH)


model = load_model()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


@app.post("/predict", response_model=FraudResponse)
def predict(request: FraudRequest):

    REQUEST_COUNT.inc()

    features = [[
        request.transaction_amount,
        request.account_age_days,
        request.num_prev_transactions,
        request.avg_transaction_amount,
        request.location_risk_score,
        request.device_risk_score,
        request.merchant_risk_score,
        request.payment_velocity,
        request.chargeback_history,
        request.failed_login_attempts
    ]]

    with PREDICTION_LATENCY.time():
        probability = model.predict_proba(features)[0][1]
        prediction = model.predict(features)[0]

    return FraudResponse(
        fraud_prediction=int(prediction),
        fraud_probability=float(probability)
    )
