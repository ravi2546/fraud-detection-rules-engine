
Fraud Prevention Java Backend (Rule-based POC)

This is a proof-of-concept (PoC) for a rule-based fraud detection engine implemented in Java.
It demonstrates how multiple independent agents (behavioral, geo, device, and decision) combine to assess transaction risk and make automated BLOCK / ALLOW decisions.

🛠 Tech Stack & Versions

Java 17

Spring Boot 3.2.0

Maven 4.0.0 (or Gradle if used)

Spring Web, Spring Boot Starter, etc.

Optional: Docker 24+

🟢 PART 1 — RUN THE SYSTEM (Step by Step)
1️⃣ Start Java Backend

📂 Go to  backend-java folder:
cd fraud-prevention-ai/backend-java

🔁 Build & run (Maven example):
mvn clean install
mvn spring-boot:run

✅ Verify

Service runs on port 8080

Open browser Swagger UI (if enabled):
http://localhost:8080/swagger-ui/index.html
Endpoint available: /api/transaction

****************Testing
Non-blocking Example
curl -X POST http://localhost:8080/api/transaction \
  -H "Content-Type: application/json" \
  -d '{
    "customerId": "C1",
    "amount": 90000,
    "merchant": "Electronics",
    "location": "India",
    "deviceId": "NEW_DEVICE"
  }'


Response:

{
  "transaction": {
    "customerId": "C1",
    "amount": 90000.0,
    "merchant": "Electronics",
    "location": "India",
    "deviceId": "NEW_DEVICE"
  },
  "behavioral_risk": 0.6,
  "behavioral_reason": "High transaction amount",
  "geo_risk": 0.1,
  "geo_reason": "Known location",
  "device_risk": 0.9,
  "device_reason": "Unknown device",
  "fraud_probability": 0.53,
  "decision": "ALLOW",
  "actions": ["TRANSACTION_APPROVED"]
}


Blocking Example
curl -X POST http://localhost:8080/api/transaction \
  -H "Content-Type: application/json" \
  -d '{
    "customerId": "C1",
    "amount": 90000,
    "merchant": "Electronics",
    "location": "Pakistan",
    "deviceId": "NEW_DEVICE"
  }'


Response:

{
  "transaction": {
    "customerId": "C1",
    "amount": 90000.0,
    "merchant": "Electronics",
    "location": "Pakistan",
    "deviceId": "NEW_DEVICE"
  },
  "behavioral_risk": 0.6,
  "behavioral_reason": "High transaction amount",
  "geo_risk": 0.85,
  "geo_reason": "Foreign transaction",
  "device_risk": 0.9,
  "device_reason": "Unknown device",
  "fraud_probability": 0.78,
  "decision": "BLOCK",
  "actions": ["TRANSACTION_BLOCKED", "CARD_FROZEN", "CUSTOMER_ALERT_SENT", "SOC_ALERT_RAISED"]
}

**************Explanation

Fraud probability is calculated as:

fraud_probability = (behavioral_risk + geo_risk + device_risk) / 3


Blocking Condition (Very Important):

if (fraud_probability > 0.7) {
    decision = "BLOCK";
} else {
    decision = "ALLOW";
}

Agents & Risk Rules

1️⃣ Behavioral Agent

Condition	Risk
amount ≤ 50,000	0.1
amount > 50,000	0.6

2️⃣ Geo Agent

Location	Risk
India	0.1
Any other country	0.85

3️⃣ Device Agent

Device	Risk
Known device	0.1
NEW_DEVICE	0.9

4️⃣ Decision Agent

Combines outputs from behavioral, geo, and device agents.

Calculates fraud_probability and decides ALLOW or BLOCK.

Determines actions to take for each transaction.

Real Examples

Blocking Transaction

amount = 90000 → 0.6

location = Pakistan → 0.85

device = NEW_DEVICE → 0.9

(0.6 + 0.85 + 0.9) / 3 = 0.78 → BLOCK


Non-blocking Transaction

amount = 90000 → 0.6

location = India → 0.1

device = NEW_DEVICE → 0.9

(0.6 + 0.1 + 0.9) / 3 = 0.53 → ALLOW


The system blocks transactions only when multiple independent agents agree the risk is high. No single signal dominates.


Future Enhancements

Replace deterministic rules with ML/LLM-powered agents

Use historical transaction data to train predictive models

Add real-time learning for adaptive risk scoring

Integrate Python AI engine & Java backend for hybrid architecture