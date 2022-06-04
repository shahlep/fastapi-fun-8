from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime


class JobsBase(BaseModel):
    title: str
    description: str
    company: str
    company_url: Optional[str]
    location: Optional[str]
    date_posted: datetime.now().date()
