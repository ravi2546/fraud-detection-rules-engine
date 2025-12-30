from state import FraudState

def device_agent(state: FraudState):
    known_devices = ["DEVICE_123"]

    if state["transaction"]["deviceId"] not in known_devices:
        return {
            "device_risk": 0.9,
            "device_reason": "Unknown device"
        }

    return {
        "device_risk": 0.1,
        "device_reason": "Trusted device"
    }
