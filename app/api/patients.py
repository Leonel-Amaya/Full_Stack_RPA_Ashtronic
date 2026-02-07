from pydantic import BaseModel
from datetime import datetime, date
from fastapi import APIRouter, Query, HTTPException
from typing import List, Optional, Dict, Any

from app.db.get_patients import get_patients
from app.db.patient_by_id import get_patient_by_id

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

class PatientDetalle(BaseModel):
    id: int
    job_id: int
    order_number: str
    patient_name: str
    patient_document: str
    date_service: datetime
    sede: str
    contrato: str
    raw_row_json: Optional[Dict[str, Any]] = None
    captured_ad: datetime

@router.get("/", response_model=List[Patient])
def get_all_patients(
    job_id: Optional[int] = Query(None, description="Filtrar por el ID del job"),
    fecha_inicio: Optional[str] = Query(None, description="Formato YYYY-MM-DD"),
    fecha_fin: Optional[str] = Query(None, description="Formato YYYY-MM-DD")
):
    
    return get_patients(job_id, fecha_inicio, fecha_fin)

@router.get("/{id}", response_model=PatientDetalle)
def get_patient_detalle(id: int):
    patient = get_patient_by_id(id)

    if not patient:
        raise HTTPException(status_code=404, detail="Paciente con ID: {id} no se encontro")

    return patient