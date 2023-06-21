from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import parse_obj_as
from typing import List, Annotated
from ..tags import Tags
from ..auth.security import get_current_active_user
from ..auth.schemas import User
from .utils import (
    create_project,
    get_project_by_id,
    update_project,
    delete_project,
    get_all_project,
)
from .schemas import ProjectOut, ProjectUpdate, ProjectIn


router = APIRouter(prefix="/projects", tags=[Tags.projects])


@router.get("/", response_model=List[ProjectOut])
async def get_projects(page_number: int = 1, page_size: int = 10):
    """A route for getting a list of projects"""
    result = await get_all_project(page_number, page_size)
    projects = parse_obj_as(List[ProjectOut], result)
    return projects


@router.get("/{project_id}", response_model=ProjectOut)
async def get_project(project_id: str):
    try:
        return await get_project_by_id(project_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post("/", response_model=ProjectOut)
async def new_project(
    project: ProjectIn,
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    try:
        return await create_project(project.dict())
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.put("/{project_id}")
async def edit_project(
    project_id: str,
    project: ProjectUpdate,
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    project = project.dict()
    project["_id"] = project_id
    try:
        return await update_project(project)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
