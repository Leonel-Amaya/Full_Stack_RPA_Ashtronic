from datetime import date
from pydantic import BaseModel


class Extract(BaseModel):
    fecha_inicial: date
    fecha_final: date
    limit: int
