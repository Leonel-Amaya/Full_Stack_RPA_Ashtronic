from fastapi import APIRouter, Query, HTTPException
from typing import List, Optional

from app.db.get_patients import get_patients
from app.db.patient_by_id import get_patient_by_id

from app.schemas.patientSchema import Patient
from app.schemas.patientDetalleSchema import PatientDetalle


router = APIRouter(prefix="/patients", tags=["Patients"])

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