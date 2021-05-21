from sqlalchemy.orm import session
from schemas.users import UserCreate
from db.models.users import UserCreate
from core.Hashing import hashed_password

def create_new _user(user: UserCreate, db:Session):
    user = User(username=user.username,
    email=user.email,
    hashed_password=Hasher.get_password_hash(user.password),
    is_active=True,
    is_superuser=False
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
