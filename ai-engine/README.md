🟢 PART 1 — RUN THE SYSTEM (Step by Step)
1️⃣ Start AI Engine (Python)
📂 Go to AI engine
cd fraud-prevention-ai/ai-engine

🔁 Activate venv
source venv/bin/activate

▶️ Run FastAPI
uvicorn main:api --reload --port 8001

✅ Verify

Open browser:

http://localhost:8001/docs


You should see:

/check-fraud endpoint

Swagger UI

💡 This itself is a WOW moment.


***********************Testing
curl -X POST http://localhost:8001/check-fraud \
  -H "Content-Type: application/json" \
  -d '{
    "customerId": "C1",
    "amount": 90000,
    "merchant": "Electronics",
    "location": "India",
    "deviceId": "NEW_DEVICE"
  }'
{"transaction":{"customerId":"C1","amount":90000.0,"merchant":"Electronics","location":"India","deviceId":"NEW_DEVICE"},"behavioral_risk":0.6,"behavioral_reason":"High transaction amount","geo_risk":0.1,"geo_reason":"Known location","device_risk":0.9,"device_reason":"Unknown device","fraud_probability":0.53,"decision":"ALLOW","actions":["TRANSACTION_APPROVED"]}%     


***********************Testing
curl -X POST http://localhost:8001/check-fraud \
  -H "Content-Type: application/json" \
  -d '{
    "customerId": "C1",
    "amount": 90000,
    "merchant": "Electronics",
    "location": "Dubai",
    "deviceId": "NEW_DEVICE"
  }'
{"transaction":{"customerId":"C1","amount":90000.0,"merchant":"Electronics","location":"Dubai","deviceId":"NEW_DEVICE"},"behavioral_risk":0.6,"behavioral_reason":"High transaction amount","geo_risk":0.85,"geo_reason":"Foreign transaction","device_risk":0.9,"device_reason":"Unknown device","fraud_probability":0.78,"decision":"BLOCK","actions":["TRANSACTION_BLOCKED","CARD_FROZEN","CUSTOMER_ALERT_SENT","SOC_ALERT_RAISED"]}%    


**************Explaination
fraud_probability =
(behavioral_risk + geo_risk + device_risk) / 3

Blocking Condition (Very Important)
if fraud_probability > 0.7:
    decision = "BLOCK"
else:
    decision = "ALLOW"

1) Behavioral Agent
Condition	        Risk
amount ≤ 50,000	    0.1
amount > 50,000	    0.6

2) Geo Agent
Location	        Risk
India	            0.1
Any other country	0.85

3) Device Agent
Device	            Risk
Known device	    0.1
NEW_DEVICE	        0.9

Real Blocking Example
amount = 90000        → 0.6
location = Dubai      → 0.85
device = NEW_DEVICE   → 0.9

(0.6 + 0.85 + 0.9) / 3 = 0.78
BLOCKED

Non-blocking Example
amount = 90000        → 0.6
location = India      → 0.1
device = NEW_DEVICE   → 0.9

(0.6 + 0.1 + 0.9) / 3 = 0.53
ALLOWED

Our system blocks transactions only when multiple independent agents agree the risk is high. No single signal is allowed to dominate.

This PoC demonstrates an agentic fraud decision architecture.
Today, agents use deterministic logic.
Tomorrow, the same agents can be powered by ML or LLMs without redesign.