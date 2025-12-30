# Fraud Detection Rules Engine

## Overview
This project is a **Proof-of-Concept (POC) for a Rule-Based Fraud Detection Engine**.  
It evaluates financial transactions in real-time and determines whether to allow or block them based on predefined rules.

The POC contains two main components:

1. **Python AI Engine (Rule-Based)**  
   - Implements behavioral, geo-location, and device risk analysis.
   - Exposes a REST API for transaction evaluation.
   - Built using **FastAPI 0.101.0** for quick demonstration.
   - Runs on **Python 3.11+**.

2. **Java Integration Service**  
   - Provides integration with backend banking systems.
   - Accepts transaction requests and communicates with the Python engine.
   - Built using **Java 17** and **Spring Boot 3.2.0**.

> ⚠️ Note: Current implementation is **rule-based**, not AI-driven. Future enhancements may include machine learning-based fraud scoring.

---

## Features

- Behavioral Risk: Flags high-value transactions.
- Geo Risk: Flags foreign or unusual locations.
- Device Risk: Flags transactions from unknown devices.
- Overall Fraud Score: Calculates combined risk and decision.
- Decision Actions: BLOCK or ALLOW transaction, with corresponding alerts.

---

## Technology Stack & Versions

| Component        | Technology      | Version       |
|-----------------|----------------|---------------|
| Python Engine    | Python         | 3.11+         |
| Python Web API   | FastAPI        | 0.101.0       |
| Python Models    | Pydantic       | 2.2.0         |
| Java Service     | Java           | 17            |
| Java Framework   | Spring Boot    | 3.2.0         |
| Build Tool       | Maven          | 4.0.0+        |
| API Communication| REST           | N/A           |
| Local Deployment | Docker (optional)| 24.0+       |

---

## Getting Started

### Python Engine
```bash
cd ai-engine
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
pip install -r requirements.txt
uvicorn main:api --reload --port 8001


### Java Service

cd java-backend
./mvnw spring-boot:run

curl -X POST http://localhost:8001/check-fraud \
  -H "Content-Type: application/json" \
  -d '{
    "customerId": "C1",
    "amount": 90000,
    "merchant": "Electronics",
    "location": "India",
    "deviceId": "NEW_DEVICE"
  }'

Project Structure
fraud-prevention-ai/
├─ ai-engine/           # Python rule-based engine
├─ java-backend/        # Java Spring Boot integration
├─ README.md
├─ .gitignore
