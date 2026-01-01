"""
Application entrypoint.

Responsibilities:
- Initialize configuration
- Start ASGI server
- Register API routes
- Initialize observability
"""

from fastapi import FastAPI
from api.v1.router import router

app = FastAPI(title="Agentic AI Platform")
app.include_router(router)
