from langgraph.graph import StateGraph
from graphs.state.compliance_state import ComplianceState
from nodes.ingestion import ingest_node
from nodes.compliance import compliance_node
from nodes.risk import risk_node
from nodes.summary import summary_node

def build_graph():
    graph = StateGraph(ComplianceState)

    graph.add_node("ingest", ingest_node)
    graph.add_node("compliance", compliance_node)
    graph.add_node("risk", risk_node)
    graph.add_node("summary", summary_node)

    graph.set_entry_point("ingest")
    graph.add_edge("ingest", "compliance")
    graph.add_edge("compliance", "risk")
    graph.add_edge("risk", "summary")

    return graph.compile()
