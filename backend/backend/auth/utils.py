from ..users.utils import get_user_by_email
from .schemas import UserInDB
from . import pwd_context


def verify_password(plain_password, hashed_password):
    """A function that verifies a password

    Returns: a boolean
            True if the password is correct
            False if the password is incorrect"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """A function that hashes a password

    Returns: a hashed password"""
    return pwd_context.hash(password)


async def get_user(email: str):
    """A function that gets a user by email

    Returns: a UserIn object if the user exists
            None if the user does not exist"""
    try:
        user = await get_user_by_email(email)
        return UserInDB(**user)
    except Exception:
        return None


async def authenticate_user(email: str, password: str):
    """A function that authenticates a user

    Returns: None if the user does not exist or the password is incorrect
            a UserIn object if the user exists and the password is correct"""
    user = await get_user(email)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user
