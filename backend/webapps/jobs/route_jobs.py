from db.repository.jobs import list_jobs
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session


templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/")
async def home(request: Request, db: Session = Depends(get_db)):
    jobs = list_jobs(db=db)
    return templates.TemplateResponse(
        "general_pages/homepage.html", {"request": request, "jobs": jobs}
    )
