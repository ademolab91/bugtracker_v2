from pydantic import BaseModel, Field
from datetime import datetime
from typing import Any


class ProjectIn(BaseModel):
    """A class that defines the schema for creating a project"""

    name: str
    description: str = ""


class ProjectOut(BaseModel):
    """A class that defines the schema for displaying project"""

    id: str = Field(alias="_id")
    name: str
    description: str
    bugs: list
    project_members: list
    created_at: datetime
    updated_at: datetime


class ProjectUpdate(ProjectIn):
    """A class that defines the schema for updating a project"""

    pass


class ProjectAddMembers(BaseModel):
    """A class that defines the schema for adding members to a project"""

    user_id: str
    project_id: str
    role: str
