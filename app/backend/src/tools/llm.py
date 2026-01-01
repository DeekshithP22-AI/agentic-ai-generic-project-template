from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-4")

async def call_llm(prompt: str) -> str:
    return await llm.apredict(prompt)
