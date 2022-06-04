from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.db.models.jobs import Job
from backend.schemas.jobs import JobCreate, ShowJobs
from backend.db.session import get_db
from backend.db.repository.jobs import create_new_job

router = APIRouter()


@router.post('/create_jobs', response_model=ShowJobs)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    owner_id = 1
    job = create_new_job(job=job, db=db,owner_id=owner_id)
    return job
