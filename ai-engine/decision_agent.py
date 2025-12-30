from state import FraudState

def decision_agent(state: FraudState):
    avg_risk = (
        state["behavioral_risk"]
        + state["geo_risk"]
        + state["device_risk"]
    ) / 3

    decision = "BLOCK" if avg_risk > 0.7 else "ALLOW"

    return {
        "fraud_probability": round(avg_risk, 2),
        "decision": decision
    }
