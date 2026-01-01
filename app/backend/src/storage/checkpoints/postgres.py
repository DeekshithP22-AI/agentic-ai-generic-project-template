from .base import CheckpointStore


class PostgresCheckpointStore(CheckpointStore):
    def __init__(self, connection):
        self.connection = connection

    def save(self, key: str, state: dict):
        raise NotImplementedError("Postgres checkpointing not implemented yet")

    def load(self, key: str):
        raise NotImplementedError("Postgres checkpointing not implemented yet")
