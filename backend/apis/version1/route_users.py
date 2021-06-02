from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.users import UserCreate, ShowUser
from db.models.users import User
from db.session import get_db
from db.repository.users import create_new_user, list_users, retreive_user, delete_user_by_id
from apis.version1.route_login import get_current_user_from_token
from typing import List


router = APIRouter()

@router.post("/", response_model=ShowUser)
def create_user(user: UserCreate, db: Session=Depends(get_db)):
    user = create_new_user(user, db)
    return user

@router.get("/all", response_model=List[ShowUser])
def retreive_all_users(db:Session = Depends(get_db)):
    users = list_users(db=db)
    return users

@router.delete("/delete/{id}")
def delete_user(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    user = retreive_user(id=id, db=db)
    if not user:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} does not exist",
        )
    print(current_user.id, current_user.username)
    if current_user.is_superuser:
        print(f"User {current_user.username}, {current_user.id} is a superuser")
        delete_user_by_id(id=id, db=db)
        return {"detail": "User successfully deleted."}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="You need to be an authorized user!!"
    )
