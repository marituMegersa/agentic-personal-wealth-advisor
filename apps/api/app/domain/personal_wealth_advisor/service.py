from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.personal_wealth_advisor.models import AgenticPersonalWealthAdvisorSession, AgenticPersonalWealthAdvisorItem
from app.domain.personal_wealth_advisor.schemas import AgenticPersonalWealthAdvisorSessionCreate, AgenticPersonalWealthAdvisorItemCreate

class AgenticPersonalWealthAdvisorService:
    @staticmethod
    def create_session(db: Session, data: AgenticPersonalWealthAdvisorSessionCreate) -> AgenticPersonalWealthAdvisorSession:
        db_obj = AgenticPersonalWealthAdvisorSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticPersonalWealthAdvisorSession:
        return db.query(AgenticPersonalWealthAdvisorSession).filter(AgenticPersonalWealthAdvisorSession.id == session_id).first()
