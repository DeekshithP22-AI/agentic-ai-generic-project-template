from llm.base import BaseLLM


class AnthropicLLM(BaseLLM):
    def generate(self, prompt: str) -> str:
        return "Anthropic response placeholder"
