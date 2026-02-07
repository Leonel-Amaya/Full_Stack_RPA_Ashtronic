from fastapi import APIRouter
from typing import List

from app.db.get_jobs import get_jobs
from app.schemas.jobSchema import Job

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.get("/", response_model=List[Job])
def get_all_jobs():
    jobs = get_jobs()
    return jobs


