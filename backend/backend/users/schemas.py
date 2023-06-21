from pydantic import BaseModel, EmailStr
from enum import Enum
from datetime import datetime

""" A schema module for inputting and outputting data from the database """


class Roles(str, Enum):
    """A class that defines the roles of the user"""

    developer = "developer"
    project_manager = "project_manager"
    qa_tester = "qa_tester"
    owner = "owner"


class UserIn(BaseModel):
    """A class that defines the schema for creating a user"""

    name: str
    email: EmailStr
    password: str
    role: str


class UserOut(BaseModel):
    """A class that defines the schema for outputting a user"""

    name: str
    email: EmailStr
    role: str
    created_at: datetime
    updated_at: datetime


class UserUpdate(BaseModel):
    """A class that defines the schema for updating a user"""

    name: str
    role: str

class UserEmail(BaseModel):
    """ A class that defines the schema for checking a user through their email """
    email: EmailStr
