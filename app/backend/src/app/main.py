from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from api.v1.router import router as api_router
from auth.azure_ad import verify_token
import logging.config
import yaml

with open("log_config.yaml") as f:
    logging.config.dictConfig(yaml.safe_load(f))

# Create FastAPI app
app = FastAPI(
    title="Agentic AI Platform",
    description="FastAPI + LangGraph integrated backend",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Include API routes
app.include_router(api_router, prefix="/api/v1", dependencies=[Depends(verify_token)])

# Health endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# You can add more custom endpoints here as needed
