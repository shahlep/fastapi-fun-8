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
