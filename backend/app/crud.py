from typing import Any, Dict, Optional, Union

from sqlmodel import Session, select

from app.core.security import get_password_hash, verify_password
from app.models import User, UserCreate, UserUpdate


def get_user_by_email(*, session: Session, email: str) -> Optional[User]:
    return session.exec(select(User).where(User.email == email)).first()


def create_user(*, session: Session, user_create: UserCreate) -> User:
    db_user = User.model_validate(user_create, update={"hashed_password": get_password_hash(user_create.password)})
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def authenticate(
    *, session: Session, email: str, password: str
) -> Optional[User]:
    user = get_user_by_email(session=session, email=email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


def update_user(
    *, session: Session, user: User, user_update: Union[UserUpdate, Dict[str, Any]]
) -> User:
    for key, value in user_update.items():
        if key == "password":
            user.hashed_password = get_password_hash(value)
        else:
            setattr(user, key, value)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user