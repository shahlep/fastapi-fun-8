from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.schemas.jobs import JobCreate, ShowJobs
from backend.db.session import get_db
from backend.db.repository.jobs import create_new_job

router = APIRouter()


@router.post('/jobs', response_model=ShowJobs)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    job = create_new_job(job, db)
    return job
