from fastapi import APIRouter
from pydantic import BaseModel
from app.db.insert_job import insert_job
from datetime import date

router = APIRouter(prefix="/rpa", tags=["RPA"])

class Extract(BaseModel):
    fecha_inicial: date
    fecha_final: date
    limit: int


@router.post("/extract")
def extract(request: Extract):
    job_id = insert_job(request.fecha_inicial, request.fecha_final, request.limit)

    return {
        "job_id": job_id,
        "fecha_inicial": request.fecha_inicial,
        "fecha_final": request.fecha_final,
        "limit": request.limit
    }