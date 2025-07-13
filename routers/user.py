from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from schemas.user import userCreate, userout
from models.user import User
from utils.auth import hash_password, verify_password, create_access_token, get_current_user

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/me", response_model=userout)
def me(Current_user: User = Depends(get_current_user)):
    return Current_user