from pydantic import BaseModel
from datetime import datetime


class Project(BaseModel):
    """A class that defines a project"""

    name: str
    description: str = ""
    bugs: list = []
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()
