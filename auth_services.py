from user_models import User
from sqlalchemy.orm import Session
from password_utils import hash_password, verify_password
from jwt_utils import create_access_token
from user_schemas import UserCreate, UserResponse

def register_user(db: Session, user: UserCreate) -> UserResponse:
    hashed_pw = hash_password(user.password)
    db_user = User(email=user.email, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return UserResponse.from_orm(db_user)

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if user and verify_password(password, user.hashed_password):
        return user
    return None

def login_user(db: Session, email: str, password: str):
    user = authenticate_user(db, email, password)
    if not user:
        return None
    token = create_access_token({"sub": user.email, "user_id": user.id})
    return token
