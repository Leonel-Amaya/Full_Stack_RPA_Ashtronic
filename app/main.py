from fastapi import FastAPI
from app.api import health, rpa, jobs

app = FastAPI(title="RPA Full Stack")

app.include_router(health.router)
app.include_router(rpa.router)
app.include_router(jobs.router)