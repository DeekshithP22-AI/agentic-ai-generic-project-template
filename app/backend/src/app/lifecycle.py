"""
Application lifecycle management.

Used for:
- Startup initialization
- Shutdown cleanup
- Resource management
"""

from fastapi import FastAPI
from observability.tracing import setup_tracing

def register_lifecycle_events(app: FastAPI):
    @app.on_event("startup")
    async def startup():
        setup_tracing()

    @app.on_event("shutdown")
    async def shutdown():
        pass
