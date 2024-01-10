from sqlalchemy.orm import Session

from models.job import JobBase

from . import models as db_models

def get_job(db: Session, job_id: int):
    return db.query(db_models.Job).filter(db_models.Job.id == job_id).first()

def create_job(db: Session, job: JobBase):
    db_job = db_models.Job(**job.model_dump())

    db.add(db_job)
    db.commit()
    db.refresh(db_job)

    return db_job

def get_jobs(db: Session, limit: int = 100):
    return db.query(db_models.Job).limit(limit).all()
