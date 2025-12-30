from state import FraudState

def geo_agent(state: FraudState):
    txn = state["transaction"]

    if txn["location"] != "India":
        return {
            "geo_risk": 0.85,
            "geo_reason": "Foreign transaction"
        }

    return {
        "geo_risk": 0.1,
            "geo_reason": "Known location"
        }
