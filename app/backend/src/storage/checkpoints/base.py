from abc import ABC, abstractmethod


class CheckpointStore(ABC):
    @abstractmethod
    def save(self, key: str, state: dict):
        pass

    @abstractmethod
    def load(self, key: str) -> dict | None:
        pass
