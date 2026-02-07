from fastapi import APIRouter
from app.db.insert_job import insert_job

from app.rpa.bot import scraper
from app.schemas.extractSchema import Extract

router = APIRouter(prefix="/rpa", tags=["RPA"])

@router.post("/extract")
def extract(request: Extract):
    job_id = insert_job(request.fecha_inicial, request.fecha_final, request.limit)

    scraper(job_id, str(request.fecha_inicial), str(request.fecha_final), request.limit)


    return {
        "job_id": job_id,
        "fecha_inicial": request.fecha_inicial,
        "fecha_final": request.fecha_final,
        "limit": request.limit
    }