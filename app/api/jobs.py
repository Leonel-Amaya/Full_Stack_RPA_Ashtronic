from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

from app.db.get_jobs import get_jobs

router = APIRouter(prefix="/jobs", tags=["Jobs"])

class Job(BaseModel):
    status: str
    error_message: Optional[str] = None
    created_at: datetime

@router.get("/", response_model=List[Job])
def get_all_jobs():
    jobs = get_jobs()
    return jobs


