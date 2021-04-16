from db.repository.users import create_new_user
from db.repository.users import get_user_by_email
from fastapi.testclient import TestClient
from schemas.users import UserCreate
from sqlalchemy.orm import Session


def user_authentication_headers(client: TestClient, email: str, password: str):
    data = {"username": email, "password": password}
    r = client.post("/login/token", data=data)
    response = r.json()
    auth_token = response["access_token"]
    headers = {"Authorization": f"Bearer {auth_token}"}
    return headers


def authentication_token_from_email(client: TestClient, email: str, db: Session):
    """
    Return a valid token for the user with given email.
    If the user doesn't exist it is created first.
    """
    password = "random-passW0rd"
    user = get_user_by_email(email=email, db=db)
    if not user:
        user_in_create = UserCreate(username=email, email=email, password=password)
        user = create_new_user(user=user_in_create, db=db)
    return user_authentication_headers(client=client, email=email, password=password)
