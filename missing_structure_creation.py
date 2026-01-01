from pathlib import Path

BASE = Path("app/backend/src")


def mkdir(path: Path):
    path.mkdir(parents=True, exist_ok=True)


def touch(path: Path, content: str = ""):
    if not path.exists():
        path.write_text(content.strip() + "\n", encoding="utf-8")


def create_core():
    base = BASE / "core"
    mkdir(base)

    touch(base / "__init__.py")
    touch(
        base / "settings.py",
        """
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Agentic AI Platform"
    environment: str = "dev"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
"""
    )

    touch(
        base / "exceptions.py",
        """
class AgenticAIException(Exception):
    \"\"\"Base exception for Agentic AI platform\"\"\"
"""
    )

    touch(
        base / "README.md",
        """
# core/

Foundational infrastructure:
- Environment configuration
- Global exceptions
"""
    )


def create_storage():
    base = BASE / "storage"
    checkpoints = base / "checkpoints"

    mkdir(checkpoints)

    touch(base / "__init__.py")
    touch(checkpoints / "__init__.py")

    touch(
        checkpoints / "base.py",
        """
class CheckpointStore:
    def save(self, key: str, state: dict):
        raise NotImplementedError

    def load(self, key: str) -> dict:
        raise NotImplementedError
"""
    )

    touch(
        checkpoints / "memory.py",
        """
class InMemoryCheckpointStore:
    def __init__(self):
        self._store = {}

    def save(self, key, state):
        self._store[key] = state

    def load(self, key):
        return self._store.get(key)
"""
    )

    touch(
        checkpoints / "postgres.py",
        """
# Placeholder for PostgreSQL-backed checkpoint store
"""
    )

    touch(
        checkpoints / "README.md",
        """
LangGraph checkpoint storage implementations.
"""
    )

    touch(base / "README.md", "State persistence and checkpointing.")


def create_llm():
    base = BASE / "llm"
    providers = base / "providers"

    mkdir(providers)

    touch(base / "__init__.py")
    touch(providers / "__init__.py")

    touch(
        base / "base.py",
        """
class BaseLLM:
    def generate(self, prompt: str) -> str:
        raise NotImplementedError
"""
    )

    touch(
        providers / "openai.py",
        """
from llm.base import BaseLLM


class OpenAILLM(BaseLLM):
    def generate(self, prompt: str) -> str:
        return "OpenAI response"
"""
    )

    touch(
        providers / "anthropic.py",
        """
from llm.base import BaseLLM


class AnthropicLLM(BaseLLM):
    def generate(self, prompt: str) -> str:
        return "Anthropic response"
"""
    )

    touch(providers / "README.md", "LLM provider implementations.")
    touch(base / "README.md", "LLM abstraction layer.")


def create_edges():
    base = BASE / "edges"
    mkdir(base)

    touch(base / "__init__.py")
    touch(
        base / "conditional.py",
        """
def route(state: dict) -> str:
    if state.get("needs_review"):
        return "human_review"
    return "executor"
"""
    )

    touch(base / "README.md", "LangGraph routing logic.")


def create_tests():
    base = Path("app/backend/tests")
    unit = base / "unit"
    integration = base / "integration"

    mkdir(unit)
    mkdir(integration)

    touch(base / "__init__.py")
    touch(unit / "__init__.py")
    touch(integration / "__init__.py")

    touch(
        base / "README.md",
        """
Test structure:
- unit/: unit tests
- integration/: integration tests
"""
    )


def create_structure():
    create_core()
    create_storage()
    create_llm()
    create_edges()
    create_tests()


if __name__ == "__main__":
    create_structure()
    print("✅ Missing structure created successfully.")
