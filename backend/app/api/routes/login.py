from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Form
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from app import crud
from app.api.deps import get_db
from app.core.config import settings
from app.core.security import create_access_token
from app.models import Token
from pydantic import BaseModel

router = APIRouter(tags=["login"])

class LoginRequest(BaseModel):
    username: str
    password: str


@router.post("/login/access-token", response_model=Token)
def login_access_token(
    session: Annotated[Session, Depends(get_db)],
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    """ OAuth2 compatible token login, get an access token for future requests """
    user = crud.authenticate(
        session=session, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return Token(
        access_token=create_access_token(user.id, expires_delta=access_token_expires),
        token_type="bearer",
    )