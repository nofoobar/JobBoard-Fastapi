from datetime import timedelta

from core.config import settings
from core.hashing import Hasher
from core.security import create_access_token
from db.repository.login import get_user
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordRequestForm
from schemas.tokens import Token
from sqlalchemy.orm import Session


router = APIRouter()


def authenticate_user(username: str, password: str, db: Session = Depends(get_db)):
    user = get_user(username=username, db=db)
    print(user)
    if not user:
        return False
    if not Hasher.verify_password(password, user.hashed_password):
        return False
    return user


@router.post("/token", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
