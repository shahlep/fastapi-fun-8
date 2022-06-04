from sqlalchemy.orm import Session
from backend.schemas.users import UserCreate
from backend.db.models.users import User
from backend.core.hashing import Hash
