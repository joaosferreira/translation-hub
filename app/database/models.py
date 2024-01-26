from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

from ..models.job import JobStatus

Base = declarative_base()

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    source = Column(String)
    target = Column(String)
    status = Column(String, default=JobStatus.UNASSIGNED)
