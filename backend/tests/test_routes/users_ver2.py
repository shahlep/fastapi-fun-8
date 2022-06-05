from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from fastapi.testclient import TestClient
import json

from backend.schemas.users import UserCreate, ShowUser
from backend.db.session import get_db
from backend.db.repository.users import create_new_user

router = APIRouter()


@router.post("/", response_model=ShowUser)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user, db)
    return user


client = TestClient(router)


def test_create_user():
    data = {"username": "test", "email": "test@example.com", "password": "123456"}
    response = client.post("/user", json.dump(data, fp=str))
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"
    assert response.json()["is_active"] == True
