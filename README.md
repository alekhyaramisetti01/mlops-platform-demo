# Fraud Risk Prediction MLOps Platform

An end-to-end **MLOps platform for fraud detection** built with FastAPI, Docker, Kubernetes, Helm, and GitHub Actions.

This project demonstrates how to build, deploy, test, and automate a machine learning inference service using production-style MLOps practices.

---

## Project Overview

This platform simulates a real-world **fraud detection system** where a machine learning model predicts fraudulent transactions.

The project covers the complete ML lifecycle, including:

- model training
- model artifact generation
- API deployment
- containerization
- Kubernetes deployment
- CI/CD automation
- automated API testing

---

## System Architecture

```mermaid
graph TD
    A[Training Pipeline<br/>ml_pipeline/train.py] --> B[Model Artifact<br/>fraud_model.joblib]
    B --> C[FastAPI Inference API<br/>app/main.py]
    C --> D[Docker Container]
    D --> E[Kubernetes Deployment]
    E --> F[Helm Chart]
    F --> G[GitHub Actions CI/CD]
    G --> H[Automated API Tests]
````

---

## Tech Stack

### Machine Learning

* Python
* Scikit-learn
* MLflow

### Backend API

* FastAPI
* Uvicorn

### MLOps Tools

* Docker
* Kubernetes
* Helm
* GitHub Actions

### Testing

* Pytest

---

## Project Structure

```text
mlops-platform-demo
│
├── app
│   ├── __init__.py
│   └── main.py
│
├── ml_pipeline
│   └── train.py
│
├── tests
│   ├── __init__.py
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
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates
│           ├── deployment.yaml
│           └── service.yaml
│
├── .github
│   └── workflows
│       └── mlops-ci.yml
│
├── Dockerfile
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Running the Project Locally

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Train the Model

```bash
python ml_pipeline/train.py
```

This generates the trained model artifact:

```text
model_artifacts/fraud_model.joblib
```

### 3. Start the FastAPI Server

```bash
uvicorn app.main:app --reload
```

The server starts at:

```text
http://127.0.0.1:8000
```

---

## API Documentation

Open the Swagger UI in your browser:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

### Metrics Endpoint

```http
GET /metrics
```

Returns service monitoring metrics.

### Fraud Prediction

```http
POST /predict
```

Example request:

```json
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
```

Example response:

```json
{
  "fraud_prediction": 0,
  "fraud_probability": 0.23
}
```

---

## Running Tests

Run automated tests with:

```bash
pytest
```

The test suite validates:

* the health endpoint
* the fraud prediction endpoint

---

## Docker Deployment

### Build Docker Image

```bash
docker build -t fraud-ml-api .
```

### Run the Container

```bash
docker run -p 8000:8000 fraud-ml-api
```

Access the API at:

```text
http://localhost:8000/docs
```

---

## Kubernetes Deployment

Apply the Kubernetes manifests:

```bash
kubectl apply -f k8s/
```

Verify the deployment:

```bash
kubectl get pods
kubectl get services
```

---

## Helm Deployment

Install the Helm chart:

```bash
helm install fraud-api helm/fraud-ml-api
```

Verify the deployment:

```bash
kubectl get pods
kubectl get svc
```

---

## CI/CD Pipeline

GitHub Actions automatically performs the following steps on every push:

1. checks out the repository
2. installs dependencies
3. runs the ML training pipeline
4. verifies model artifact generation
5. executes automated API tests
6. builds the Docker image

This ensures reproducibility and reliability for the ML system.

---

## Author

**Alekhya Ramisetti**

