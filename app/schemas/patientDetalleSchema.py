from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel


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