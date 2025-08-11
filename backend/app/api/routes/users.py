from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app import crud
from app.api.deps import get_db
from app.models import Message, User, UserCreate, UserPublic

router = APIRouter(tags=["users"])


@router.post("/users/", response_model=UserPublic)
def create_user(
    *, session: Annotated[Session, Depends(get_db)], user_create: UserCreate
) -> User:
    """ Create new user """
    user = crud.get_user_by_email(session=session, email=user_create.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = crud.create_user(session=session, user_create=user_create)
    return user