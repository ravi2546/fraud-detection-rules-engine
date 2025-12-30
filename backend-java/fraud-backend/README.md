
****************Tesing
curl -X POST http://localhost:8080/api/transaction \
  -H "Content-Type: application/json" \
  -d '{
    "customerId": "C1",
    "amount": 90000,
    "merchant": "Electronics",
    "location": "India",
    "deviceId": "NEW_DEVICE"
  }'

  {"transaction":{"customerId":"C1","amount":90000.0,"merchant":"Electronics","location":"India","deviceId":"NEW_DEVICE"},"behavioral_risk":0.6,"behavioral_reason":"High transaction amount","geo_risk":0.1,"geo_reason":"Known location","device_risk":0.9,"device_reason":"Unknown device","fraud_probability":0.53,"decision":"ALLOW","actions":["TRANSACTION_APPROVED"]}% 

****************Tesing
   curl -X POST http://localhost:8080/api/transaction \
  -H "Content-Type: application/json" \
  -d '{
    "customerId": "C1",
    "amount": 90000,
    "merchant": "Electronics",
    "location": "Pakistan",
    "deviceId": "NEW_DEVICE"
  }'
{"transaction":{"customerId":"C1","amount":90000.0,"merchant":"Electronics","location":"Pakistan","deviceId":"NEW_DEVICE"},"behavioral_risk":0.6,"behavioral_reason":"High transaction amount","geo_risk":0.85,"geo_reason":"Foreign transaction","device_risk":0.9,"device_reason":"Unknown device","fraud_probability":0.78,"decision":"BLOCK","actions":["TRANSACTION_BLOCKED","CARD_FROZEN","CUSTOMER_ALERT_SENT","SOC_ALERT_RAISED"]}%                           