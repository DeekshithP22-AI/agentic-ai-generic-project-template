from tools.llm import call_llm

async def compliance_node(state):
    result = await call_llm(
        f"Check compliance issues in:\n{state['document']}"
    )
    state["issues"] = result.splitlines()
    return state
