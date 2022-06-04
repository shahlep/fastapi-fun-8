from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime


class JobsBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    company: Optional[str] = None
    company_url: Optional[str] = None
    location: Optional[str] = None
    date_posted: Optional[str] = datetime.now().date()


class JobCreate(JobsBase):
    title: str
    description: str
    company: str
    location: str


class ShowJobs(JobsBase):
    title: str
    company: str
    location: str
    date_posted: date
    description: Optional[str]
    company_url: Optional[str]

    class Config:
        orm_mode = True
