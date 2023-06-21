from uuid import uuid4
from ..projects.utils import get_project_by_id, update_project_bugs
from .models import Bug
from . import bugs


async def create_bug(bug: dict) -> dict:
    """A function for creating a bug instance"""
    if await get_project_by_id(bug.get("project_id", None)):
        bug = Bug(**bug)
        result = await bugs.insert_one(bug.dict())
        bug = await bugs.find_one({"_id": result.inserted_id})
        # Change the id
        bug["_id"] = str(uuid4())
        new_result = await bugs.insert_one(bug)
        await bugs.delete_one({"_id": result.inserted_id})
        bug = await bugs.find_one({"_id": new_result.inserted_id})
        if bug:
            await update_project_bugs(project_id=bug["project_id"], bug_id=bug["_id"])
            return bug
        raise Exception("Bug could not be reported")
    raise Exception("Project does not exist")


async def get_bug_by_id(bug_id: str) -> dict:
    """A function for reading bug"""
    bug = await bugs.find_one({"_id": bug_id})
    if bug:
        return bug
    raise Exception("Bug not found")


async def get_all_bug(page_number: int, page_size: int) -> list:
    """A function for reading all the bug in the database"""
    skip_count = (page_number - 1) * page_size
    all_bug = bugs.find().skip(skip_count).limit(page_size)
    result = await all_bug.to_list(length=page_size)
    return result


async def get_all_bug_in_a_project(
    project_id: str, page_number: int, page_size: int
) -> list:
    """A function for reading all the bug of a particular project"""
    project = await get_project_by_id(project_id)
    if project:
        skip_count = (page_number - 1) * page_size
        all_project_bug = (
            bugs.find({"project_id": project_id}).skip(skip_count).limit(page_size)
        )
        result = await all_project_bug.to_list(length=page_size)
        return result
    raise Exception("Project not found or does not exist")


async def update_bug(bug: dict) -> dict:
    """A function for updating a bug"""
    db_bug = await bugs.find_one({"_id": bug["_id"]})
    if db_bug:
        for key, value in bug.items():
            if value == "" or value == None:
                bug[key] = db_bug[key]
        await bugs.update_one({"_id": bug["_id"]}, {"$set": bug})
        bug = await bugs.find_one({"_id": bug["_id"]})
        return bug
    raise Exception("Bug does not exist")


async def delete_bug(bug_id: str) -> None:
    pass
