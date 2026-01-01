from langgraph.graph import StateGraph
from graphs.state.compliance_state import ComplianceState
from nodes.compliance import compliance_node
from graphs.subgraphs.verification import verification_subgraph

def build_compliance_agent():
    graph = StateGraph(ComplianceState)

    graph.add_node("compliance", compliance_node)
    graph.add_node("verify", verification_subgraph)

    graph.set_entry_point("compliance")
    graph.add_edge("compliance", "verify")

    return graph.compile()
