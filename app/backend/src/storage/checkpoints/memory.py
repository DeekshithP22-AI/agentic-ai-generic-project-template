from .base import CheckpointStore


class InMemoryCheckpointStore(CheckpointStore):
    def __init__(self):
        self._store = {}

    def save(self, key: str, state: dict):
        self._store[key] = state

    def load(self, key: str):
        return self._store.get(key)
