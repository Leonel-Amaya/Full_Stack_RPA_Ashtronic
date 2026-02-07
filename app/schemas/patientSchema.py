from datetime import datetime
from pydantic import BaseModel


class Patient(BaseModel):
    job_id: int
    order_number: str
    patient_name: str
    patient_document: str
    date_service: datetime
    sede: str
    contrato: str
    captured_ad: datetime