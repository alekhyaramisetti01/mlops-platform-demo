# Fraud Risk Prediction MLOps Platform

An end-to-end MLOps platform for fraud detection built with FastAPI, Docker, Kubernetes, Helm, and GitHub Actions.

This project demonstrates how to build, deploy, and monitor a machine learning inference service in a production-style environment.

---

# Architecture

Training Pipeline
↓
Model Artifact
↓
FastAPI Inference API
↓
Docker Container
↓
Kubernetes Deployment
↓
Helm Chart
↓
GitHub Actions CI/CD
↓
Automated API Tests

---

# Tech Stack

- Python
- FastAPI
- Scikit-learn
- Pytest
- Docker
- Kubernetes
- Helm
- GitHub Actions
- MLflow

---

# Project Structure
mlops-platform-demo
│
├── app
│   └── main.py
│
├── ml_pipeline
│   └── train.py
│
├── tests
│   └── test_api.py
│
├── model_artifacts
│   └── fraud_model.joblib
│
├── k8s
│   ├── deployment.yaml
│   └── service.yaml
│
├── helm
│   └── fraud-ml-api
│
├── .github
│   └── workflows
│
├── Dockerfile
├── requirements.txt
└── README.md
Running the Project Locally
Install Dependencies
pip install -r requirements.txt
Train the Model
python ml_pipeline/train.py

This generates the trained model:

model_artifacts/fraud_model.joblib
Start the FastAPI Server
uvicorn app.main:app --reload

Server will start at:

http://127.0.0.1:8000
API Documentation

Open the Swagger UI:

http://127.0.0.1:8000/docs
API Endpoints
Health Check
GET /health

Response:

{
 "status": "ok"
}
Metrics Endpoint
GET /metrics

Returns service monitoring metrics.

Fraud Prediction
POST /predict

Example request:

{
 "transaction_amount": 500,
 "account_age_days": 200,
 "num_prev_transactions": 30,
 "avg_transaction_amount": 200,
 "location_risk_score": 0.6,
 "device_risk_score": 0.4,
 "merchant_risk_score": 0.3,
 "payment_velocity": 2,
 "chargeback_history": 0,
 "failed_login_attempts": 1
}

Example response:

{
 "fraud_prediction": 0,
 "fraud_probability": 0.23
}
Running Tests

Run automated tests using:

pytest

Tests validate:

Health endpoint

Fraud prediction endpoint

Docker Deployment

Build Docker image:

docker build -t fraud-ml-api .

Run container:

docker run -p 8000:8000 fraud-ml-api

Access API at:

http://localhost:8000/docs
Kubernetes Deployment

Apply Kubernetes manifests:

kubectl apply -f k8s/

Check deployment:

kubectl get pods
kubectl get services
Helm Deployment

Install Helm chart:

helm install fraud-api helm/fraud-ml-api

Verify deployment:

kubectl get pods
kubectl get svc
CI/CD Pipeline

GitHub Actions automatically performs the following steps on every push:

Checkout repository

Install dependencies

Run ML training pipeline

Verify model artifact

Execute automated API tests

Build Docker image

This ensures reproducibility and reliability for the ML system.