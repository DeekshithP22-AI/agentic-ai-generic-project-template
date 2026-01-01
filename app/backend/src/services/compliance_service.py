from agents.agent_one.graph import build_compliance_agent
from agents.agent_two.graph import build_risk_agent

class ComplianceService:
    def __init__(self, user):
        self.user = user
        self.compliance_agent = build_compliance_agent()
        self.risk_agent = build_risk_agent()

    async def run(self, request):
        compliance_result = await self.compliance_agent.ainvoke({
            "document": request.document
        })

        risk_result = await self.risk_agent.ainvoke({
            "document": request.document
        })

        return {
            "compliance_issues": compliance_result["issues"],
            "risks": risk_result["risks"]
        }
