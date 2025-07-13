from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from schemas.user import userCreate, userout
from models.user import User
from utils.auth import hash_password, verify_password, create_access_token

router = APIRouter()

@router.post("/register", response_model=userout)
def register(user: userCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    hashed_pw = hash_password(user.password)
    new_user = User(
        email=user.email,
        username=user.username,
        hashed_password=hashed_pw
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_access_token(data={"sub": str(user.id)})

    return {
        "access_token": token,
        "token_type": "bearer"
    }

