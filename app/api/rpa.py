from fastapi import APIRouter
from pydantic import BaseModel
from app.db.insert_job import insert_job
from datetime import datetime

router = APIRouter(prefix="/rpa", tags=["RPA"])

class Extract(BaseModel):
    fecha_inicial: str
    fecha_final: str
    limit: int


@router.post("/extract")
def extract(request: Extract):
    fecha_inicial = datetime.strptime(request.fecha_inicial, "%Y-%m-%d")
    fecha_final = datetime.strptime(request.fecha_final, "%Y-%m-%d")


    job_id = insert_job(fecha_inicial, fecha_final, request.limit)

    return {
        "job_id": job_id,
        "fecha_inicial": request.fecha_inicial,
        "fecha_final": request.fecha_final,
        "limit": request.limit
    }