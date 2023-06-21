from pydantic import BaseModel, Field
from datetime import datetime


class Bug(BaseModel):
    """A class that defines a bug"""

    title: str = ""
    description: str = ""
    steps_to_reproduce: str = ""
    priority: str = ""
    status: str = ""
    assigned_developers_id: list = []
    reporter_id: str = ""
    files: list = []
    project_id: str = ""
    comments: list = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)