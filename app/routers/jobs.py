from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db
from models.job import Job, JobBase
from database import operations 

router = APIRouter(
    prefix="/jobs"
)

@router.post("/", response_model=Job)
def create_job(job: JobBase, db: Session = Depends(get_db)):
    db_job = operations.create_job(db, job)
    return db_job

@router.get("/{job_id}", response_model=Job)
def get_job(job_id: int, db: Session = Depends(get_db)):
    db_job = operations.get_job(db, job_id)
    if db_job is None:
        raise HTTPException(status_code=404, detail=f"Job with Id {job_id} does not exist")
    return db_job

@router.get("/", response_model=list[Job])
def get_jobs(limit: int = 100, db: Session = Depends(get_db)):
    db_jobs = operations.get_jobs(db, limit=limit)
    return db_jobs
