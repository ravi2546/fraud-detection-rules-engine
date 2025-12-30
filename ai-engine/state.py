# state.py
from typing import TypedDict, Optional, Dict, Any

class FraudState(TypedDict, total=False):
    transaction: Dict[str, Any]

    behavioral_risk: float
    behavioral_reason: str

    geo_risk: float
    geo_reason: str

    device_risk: float
    device_reason: str

    fraud_probability: float
    decision: str
    actions: list
