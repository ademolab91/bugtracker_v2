from fastapi import APIRouter, HTTPException, status, Depends
from typing import List, Annotated
from pydantic import parse_obj_as
from ..tags import Tags
from ..auth.schemas import User
from ..auth.security import get_current_active_user
from .utils import *
from .schemas import *


router = APIRouter(prefix="/bugs", tags=[Tags.bugs])


@router.get("/", response_model=List[BugOut])
async def get_bugs(page_number: int = 1, page_size: int = 10):
    """A route for getting all bugs from database"""
    try:
        result = await get_all_bug(page_number, page_size)
        return parse_obj_as(List[BugOut], result)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/{bug_id}", response_model=BugOut)
async def get_bug(bug_id: str):
    """A route for getting a single bug by it's ID"""
    try:
        return await get_bug_by_id(bug_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post("/", response_model=BugOut)
async def report_bug(
    bug: BugIn, current_user: Annotated[User, Depends(get_current_active_user)]
):
    """A route for reporting a bug"""
    try:
        return await create_bug(bug.dict())
    except Exception as e:
        if e == "Bug could not be reported":
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.put("/{bug_id}", response_model=BugOut)
async def modify_bug(
    bug_id: str,
    bug: BugUpdate,
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    """A route for modifying a bug"""
    try:
        bug = bug.dict()
        bug["_id"] = bug_id
        print(bug)
        return await update_bug(bug)
    except Exception as e:
        print(bug)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
