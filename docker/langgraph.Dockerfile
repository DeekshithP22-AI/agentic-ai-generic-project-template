# ---------------------------------------
# Official LangGraph API base image
# ---------------------------------------
    FROM ghcr.io/langchain-ai/langgraph-api:latest

    # ---------------------------------------
    # Set working directory
    # ---------------------------------------
    WORKDIR /app
    
    # ---------------------------------------
    # Copy backend source
    # ---------------------------------------
    COPY ./src /app/src
    
    # ---------------------------------------
    # Copy configuration
    # ---------------------------------------
    COPY langgraph.json /app/langgraph.json
    COPY pyproject.toml poetry.lock* /app/
    
    # ---------------------------------------
    # Install additional dependencies
    # (if required beyond base image)
    # ---------------------------------------
    RUN pip install --no-cache-dir \
        azure-identity \
        fastapi \
        uvicorn
    
    # ---------------------------------------
    # Expose LangGraph API port
    # ---------------------------------------
    EXPOSE 8000
    
    # ---------------------------------------
    # Start LangGraph API
    # ---------------------------------------
    CMD ["langgraph", "serve", "--config", "langgraph.json"]
    