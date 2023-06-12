from fastapi import Depends, HTTPException, status, Security
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from typing import Annotated
from datetime import datetime, timedelta
from jose import JWTError, jwt
from pydantic import ValidationError
from .. import settings
from .utils import get_user
from .schemas import TokenData, User
from .auth_scopes import auth_scopes
from .role_scope import RoleScope


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login", scopes=auth_scopes)


def create_access_token(data: dict):
    """A function that creates an access token and stores it

    Returns: a string of the access token"""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.secret_key, algorithm=settings.algorithm
    )
    return encoded_jwt


async def get_current_user(
    security_scopes: SecurityScopes, token: Annotated[str, Depends(oauth2_scheme)]
):
    """A function that gets the current user

    Returns: a UserIn object of the current user

    Raises: HTTPException 401 if the token is invalid"""
    if security_scopes.scopes:
        authenticate_value = f"Bearer scope='{security_scopes.scope_str}'"
    else:
        authenticate_value = "Bearer"
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=["HS256"])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_scopes = payload.get("scopes", [])
        token_data = TokenData(scopes=token_scopes, email=email)
    except (JWTError, ValidationError):
        raise credentials_exception
    user = await get_user(email=token_data.email)
    if user is None:
        raise credentials_exception
    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not enough permissions",
                headers={"WWW-Authenticate": authenticate_value},
            )
    return user


async def get_current_active_user(
    current_user: Annotated[
        User, Security(get_current_user, scopes=RoleScope.developer.value)
    ]
):
    """A function that gets the current active user

    Returns: a UserIn object of the current active user

    Raises: HTTPException 400 if the user is inactive"""
    if current_user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user"
        )
    return current_user
