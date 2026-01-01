# ==========================================================
# Backend Dockerfile – Agentic AI Platform
# FastAPI + LangGraph + Azure AD + Poetry
# ==========================================================

# ------------------------------
# Base image
# ------------------------------
    FROM python:3.10-slim AS base

    # ------------------------------
    # Environment variables
    # ------------------------------
    ENV PYTHONDONTWRITEBYTECODE=1 \
        PYTHONUNBUFFERED=1 \
        POETRY_VERSION=1.7.1 \
        POETRY_NO_INTERACTION=1 \
        POETRY_VIRTUALENVS_CREATE=false
    
    # ------------------------------
    # System dependencies
    # ------------------------------
    RUN apt-get update && apt-get install -y \
        build-essential \
        curl \
        git \
        ca-certificates \
        && rm -rf /var/lib/apt/lists/*
    
    # ------------------------------
    # Install Poetry
    # ------------------------------
    RUN curl -sSL https://install.python-poetry.org | python3 -
    
    ENV PATH="/root/.local/bin:$PATH"
    
    # ------------------------------
    # Set working directory
    # ------------------------------
    WORKDIR /app
    
    # ------------------------------
    # Copy dependency files first
    # (enables Docker layer caching)
    # ------------------------------
    COPY backend/pyproject.toml backend/poetry.lock* ./backend/
    
    # ------------------------------
    # Install dependencies
    # ------------------------------
    WORKDIR /app/backend
    RUN poetry install --no-root
    
    # ------------------------------
    # Copy source code
    # ------------------------------
    COPY backend/src ./src
    
    # ------------------------------
    # Expose port
    # ------------------------------
    EXPOSE 8000
    
    # ------------------------------
    # Run application
    # ------------------------------
    CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
    