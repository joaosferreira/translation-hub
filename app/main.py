from fastapi import FastAPI
from sqlalchemy import create_engine

from .database import models
from .dependencies import engine
from .routers import jobs

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(jobs.router)

@app.get("/")
async def root():
    return {}