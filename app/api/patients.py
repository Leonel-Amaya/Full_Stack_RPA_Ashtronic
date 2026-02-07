from pydantic import BaseModel
from datetime import datetime, date
from fastapi import APIRouter, Query
from typing import List, Optional

from app.db.get_patients import get_patients

router = APIRouter(prefix="/patients", tags=["Patients"])

class Patient(BaseModel):
    job_id: int
    order_number: str
    patient_name: str
    patient_document: str
    date_service: datetime
    sede: str
    contrato: str
    captured_ad: datetime

@router.get("/", response_model=List[Patient])
def get_all_patients(
    job_id: Optional[int] = Query(None, description="Filtrar por el ID del job"),
    fecha_inicio: Optional[str] = Query(None, description="Formato YYYY-MM-DD"),
    fecha_fin: Optional[str] = Query(None, description="Formato YYYY-MM-DD")
):
    
    return get_patients(job_id, fecha_inicio, fecha_fin)