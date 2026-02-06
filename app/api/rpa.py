from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/rpa", tags=["RPA"])

class Extract(BaseModel):
    fecha_inicial: str
    fecha_final: str
    limit: int


@router.post("/extract")
def extract(request: Extract):
    return {
        "fecha_inicial": request.fecha_inicial,
        "fecha_final": request.fecha_final,
        "limit": request.limit
    }