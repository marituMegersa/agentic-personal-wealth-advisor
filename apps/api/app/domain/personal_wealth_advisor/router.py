from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.personal_wealth_advisor.schemas import AgenticPersonalWealthAdvisorSessionCreate, AgenticPersonalWealthAdvisorSessionResponse
from app.domain.personal_wealth_advisor.service import AgenticPersonalWealthAdvisorService

router = APIRouter(prefix="/api/v1/personal_wealth_advisor", tags=["Agentic Personal Wealth Advisor Domain"])

@router.post("/sessions", response_model=AgenticPersonalWealthAdvisorSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticPersonalWealthAdvisorSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Personal Wealth Advisor.
    """
    return AgenticPersonalWealthAdvisorService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticPersonalWealthAdvisorSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticPersonalWealthAdvisorService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
