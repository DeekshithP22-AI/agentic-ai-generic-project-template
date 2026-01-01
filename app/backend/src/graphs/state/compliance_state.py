from typing import TypedDict, List

class ComplianceState(TypedDict):
    document: str
    issues: List[str]
    risks: List[str]
    verified: bool
