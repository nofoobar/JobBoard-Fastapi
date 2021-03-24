from db.models.users import User
from sqlalchemy.orm import Session


def get_user(username: str, db: Session):
    user = db.query(User).filter(User.email == username).first()
    return user
