from sqlalchemy.orm import Session
from backend.schemas.users import UserCreate
from backend.db.models.users import User
from backend.core.hashing import Hash


def create_new_user(user: UserCreate, db: Session):
    user = User(
        username=user.username,
        email=user.email,
        hashed_password=Hash.get_hash_password(user.password),
        is_active=True,
        is_superuser=False,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
