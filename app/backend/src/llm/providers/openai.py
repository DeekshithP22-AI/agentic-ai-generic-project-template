from llm.base import BaseLLM


class OpenAILLM(BaseLLM):
    def generate(self, prompt: str) -> str:
        return "OpenAI response placeholder"
