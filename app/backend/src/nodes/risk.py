from tools.llm import call_llm

async def risk_node(state):
    result = await call_llm(
        f"Identify risks in:\n{state['document']}"
    )
    state["risks"] = result.splitlines()
    return state
