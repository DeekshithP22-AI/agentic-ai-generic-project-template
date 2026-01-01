async def ingest_node(state):
    return {
        **state,
        "extracted_text": state["document"]
    }
