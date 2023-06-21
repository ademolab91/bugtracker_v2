from pydantic import BaseModel, Field
from datetime import datetime


class BugIn(BaseModel):
    """A class that defines the schema for reporting a new bug"""

    title: str
    description: str = ""
    steps_to_reproduce: str = ""
    files: list = []
    project_id: str


class BugOut(BaseModel):
    """A class that defines the schema for displaying a bug"""

    id: str = Field(alias="_id")
    title: str
    description: str
    steps_to_reproduce: str
    priority: str
    status: str
    assigned_developers_id: list
    reporter_id: str
    files: list
    project_id: str
    comments: list
    created_at: datetime
    updated_at: datetime


class BugUpdate(BaseModel):
    """A class that defines the schema for updating a bug"""

    title: str = ""
    description: str = ""
    steps_to_reproduce: str = ""
