from fastapi import APIRouter
from services.compliance_service import ComplianceWorkflowService
from api.v1.schemas import ComplianceRequest

router = APIRouter()

@router.post("/compliance/run")
async def run_compliance(req: ComplianceRequest):
    service = ComplianceWorkflowService()
    return await service.run(req.document)
