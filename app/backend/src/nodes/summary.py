from tools.llm import call_llm
from prompts.summary_prompt import SUMMARY_PROMPT

async def summary_node(state):
    summary = await call_llm(
        SUMMARY_PROMPT.format(
            issues=state["compliance_issues"],
            risks=state["risks"]
        )
    )
    return {
        **state,
        "summary": summary
    }
