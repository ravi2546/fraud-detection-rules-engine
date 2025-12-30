from state import FraudState

def behavioral_agent(state: FraudState):
    txn = state["transaction"]

    risk = 0.1
    reason = "Normal behavior"

    if txn["amount"] > 50000:
        risk = 0.6
        reason = "High transaction amount"

    # ✅ UPDATE shared state (do NOT replace it)
    state["behavioral_risk"] = risk
    state["behavioral_reason"] = reason
    print("STATE AT BEHAVIOR:", state)
    return state
