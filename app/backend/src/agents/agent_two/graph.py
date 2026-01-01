from langgraph.graph import StateGraph
from graphs.state.compliance_state import ComplianceState
from nodes.risk import risk_node

def build_risk_agent():
    graph = StateGraph(ComplianceState)

    graph.add_node("risk", risk_node)
    graph.set_entry_point("risk")

    return graph.compile()
