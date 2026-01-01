from fastapi import APIRouter
from api.v1.agents import router as agents_router
from api.v1.health import router as health_router

router = APIRouter()
router.include_router(agents_router, prefix="/agents")
router.include_router(health_router, prefix="/health")
