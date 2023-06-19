from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from ..tags import Tags
from ..auth.security import get_current_active_user
from ..auth.schemas import User
from .schemas import UserOut, UserUpdate, UserIn, UserEmail
from .utils import create_user, get_user_by_id, update_user, get_user_by_email


router = APIRouter(prefix="/users", tags=[Tags.users])


@router.get("/me", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    """Get the current user"""
    return current_user


@router.get("/{user_id}", response_model=UserOut)
async def get_user(user_id: str):
    """Get a user by id"""
    try:
        return await get_user_by_id(user_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    

@router.post("/email", response_model=UserOut)
async def get_user_with_email(user: UserEmail):
    """ Get user by email """
    try:
        return await get_user_by_email(user.email)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.put("/me", response_model=User)
async def update_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)], user: UserUpdate
):
    """Update the current user"""
    try:
        return await update_user(current_user.email, user.dict())
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/signup", response_model=UserOut)
async def signup(user: UserIn):
    """Create a new user"""
    try:
        return await create_user(user.dict())
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
