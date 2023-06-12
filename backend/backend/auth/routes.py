from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from ..tags import Tags
from .schemas import Token
from .utils import authenticate_user
from .security import create_access_token


router = APIRouter(prefix="/auth", tags=[Tags.auth])


@router.post("/login", response_model=Token)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    """A function that logs in a user

    Returns: a Token object with the access token

    Raises: HTTPException if the credentials are invalid"""

    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user.email, "scopes": form_data.scopes}
    )
    return {"access_token": access_token, "token_type": "bearer"}
