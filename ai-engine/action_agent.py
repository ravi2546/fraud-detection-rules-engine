from state import FraudState

def action_agent(state: FraudState):
    if state["decision"] == "BLOCK":
        return {
            "actions": [
                "TRANSACTION_BLOCKED",
                "CARD_FROZEN",
                "CUSTOMER_ALERT_SENT",
                "SOC_ALERT_RAISED"
            ]
        }

    return {
        "actions": ["TRANSACTION_APPROVED"]
    }
