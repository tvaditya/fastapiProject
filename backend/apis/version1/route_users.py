from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.users import UserCreate, ShowUser
from db.session import get_db
from db.repository.users import create_new_user, list_users
from typing import List


router = APIRouter()

@router.post("/", response_model=ShowUser)
def create_user(user: UserCreate, db: Session=Depends(get_db)):
    user = create_new_user(user, db)
    return user

@router.get("/all", response_model=List[ShowUser])
def retreive_all_jobs(db:Session = Depends(get_db)):
    users = list_users(db=db)
    return users
