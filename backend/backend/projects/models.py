from pydantic import BaseModel, Field
from datetime import datetime
from uuid import uuid4


class Project(BaseModel):
    """A class that defines a project"""

    name: str
    description: str
    bugs: list = []
    project_members: list = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class Comment(BaseModel):
    """A class that defines a comment"""

    content: str
    author_id: str
    bug_id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


class File(BaseModel):
    """A class that defines a file"""

    filename: str
    url: str
    bug_id: str


class ProjectMember(BaseModel):
    """A class that defines each user in a project"""

    user_id: str
    project_id: str
    role: str
