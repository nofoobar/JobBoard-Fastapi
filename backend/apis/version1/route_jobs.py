from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status

from db.session import get_db
from db.models.jobs import Job
from schemas.jobs import JobCreate,ShowJob
from db.repository.jobs import create_new_job

router = APIRouter()


@router.post("/create-job/",response_model=ShowJob)
def create_job(job: JobCreate,db: Session = Depends(get_db)):
    current_user = 1
    job = create_new_job(job=job,db=db,owner_id=current_user)
    return job
