from enum import Enum

from pydantic import BaseModel

class Language(str, Enum):
    EN = "en"
    PT = "pt"

class JobStatus(str, Enum):
    ASSIGNED = "ASSIGNED"
    COMPLETED = "COMPLETED"
    UNASSIGNED = "UNASSIGNED"

class JobBase(BaseModel):
    text: str
    source: Language
    target: Language

class Job(JobBase):
    id: int
    status: JobStatus = JobStatus.UNASSIGNED

    class Config:
        from_attributes = True
