from fastapi import APIRouter
from fastapi import Request,Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from db.repository.jobs import list_jobs
from db.session import get_db



templates = Jinja2Templates(directory="templates")
general_pages_router = APIRouter()


@general_pages_router.get("/")
async def home(request: Request,db: Session = Depends(get_db)):
    jobs = list_jobs(db=db)
    return templates.TemplateResponse(
        "general_pages/homepage.html", {"request": request,"jobs":jobs}
    )
