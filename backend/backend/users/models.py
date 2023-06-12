from pydantic import BaseModel, EmailStr
from datetime import datetime


class User(BaseModel):
    """A class that defines a user"""

    name: str = None
    hashed_password: str
    email: EmailStr
    role: str = None
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()
