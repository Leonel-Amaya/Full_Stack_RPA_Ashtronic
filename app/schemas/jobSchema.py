from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Job(BaseModel):
    status: str
    error_message: Optional[str] = None
    created_at: datetime