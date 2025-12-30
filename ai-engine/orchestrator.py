from langgraph.graph import StateGraph
from state import FraudState
from behavioral_agent import behavioral_agent
from geo_agent import geo_agent
from device_agent import device_agent
from decision_agent import decision_agent
from action_agent import action_agent

graph = StateGraph(FraudState)

graph.add_node("behavior", behavioral_agent)
graph.add_node("geo", geo_agent)
graph.add_node("device", device_agent)
graph.add_node("decision", decision_agent)
graph.add_node("action", action_agent)

graph.set_entry_point("behavior")

graph.add_edge("behavior", "geo")
graph.add_edge("geo", "device")
graph.add_edge("device", "decision")
graph.add_edge("decision", "action")

app = graph.compile()
