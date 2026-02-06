from fastapi import FastAPI
from app.api import health

app = FastAPI(title="RPA Full Stack")

app.include_router(health.router)