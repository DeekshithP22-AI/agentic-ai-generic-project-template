from fastapi import APIRouter, Depends
from auth.azure_ad import get_current_user
from services.compliance_service import ComplianceService
from api.v1.schemas import AnalyzeRequest, AnalyzeResponse

router = APIRouter()

@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze(
    req: AnalyzeRequest,
    user=Depends(get_current_user)
):
    service = ComplianceService(user)
    return await service.run(req)
