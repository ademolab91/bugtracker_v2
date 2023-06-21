from pydantic import EmailStr
from uuid import uuid4
from .models import User
from .schemas import UserIn, UserUpdate
from ..auth import pwd_context
from . import users

""" A module that defines the utilities for the users app """


async def create_user(user: dict):
    """A function that creates a user

    Returns: a dictionary of the newly created user"""
    if not await users.find_one({"email": user["email"]}):
        user["hashed_password"] = pwd_context.hash(user["password"])
        user.pop("password")
        user = User(**user)
        result = await users.insert_one(user.dict())
        user = await users.find_one({"_id": result.inserted_id})
        # change the id from ObjectId to uuid4
        user["_id"] = str(uuid4())
        new_result = await users.insert_one(user)
        await users.delete_one({"_id": result.inserted_id})
        user = await users.find_one({"_id": new_result.inserted_id})
        return user
    raise Exception("Email already exists")


async def get_user_by_email(email: str):
    """A function that gets a user by email

    Returns: a dictionary of the user"""
    user = await users.find_one({"email": email})
    if user:
        return user
    raise Exception("User not found")


async def get_user_by_id(user_id: str):
    """A function that gets a user by id

    Returns: a dictionary of the user"""
    user = await users.find_one({"_id": user_id})
    if user:
        return user
    raise Exception("User not found")


async def update_user(email: EmailStr, user: dict):
    """A function that updates a user by email

    Returns: a dictionary of the updated user"""
    if await users.find_one({"email": email}):
        await users.update_one({"email": email}, {"$set": user})
        user = await users.find_one({"email": email})
        return user
    raise Exception("User not found")
