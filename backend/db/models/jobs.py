import datetime

from sqlalchemy import Column, Integer, Boolean, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from backend.db.base_class import Base


class Job(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    company = Column(String, nullable=False)
    company_url = Column(String)
    location = Column(String, nullable=False)
    date_posted = Column(Date)
    is_active = Column(Boolean, default=False)
    # foreign key
    owner_id = Column(Integer, ForeignKey("user.id"))
    # relationship
    owner = relationship("User", back_populates="jobs")
