from pydantic import BaseModel

class ComplianceRequest(BaseModel):
    document_text: str

class ComplianceResponse(BaseModel):
    summary: str
    risks: list[str]
    compliance_issues: list[str]
