from fastapi import FastAPI
from pydantic import BaseModel
from state import FraudState
from orchestrator import app as fraud_graph

api = FastAPI()

class TransactionRequest(BaseModel):
    customerId: str
    amount: float
    merchant: str
    location: str
    deviceId: str

@api.post("/check-fraud")
def check_fraud(request: TransactionRequest):
    state = FraudState({
        "transaction": request.dict()
    })

    result = fraud_graph.invoke(state)
    return result
