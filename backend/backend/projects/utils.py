from uuid import uuid4
from . import projects
from .models import Project


async def create_project(project: dict):
    """A function for creating a new project"""
    project = Project(**project)
    result = await projects.insert_one(project.dict())
    project = await projects.find_one({"_id": result.inserted_id})
    # change the id to uuid4
    project["_id"] = str(uuid4())
    new_result = await projects.insert_one(project)
    await projects.delete_one({"_id": result.inserted_id})
    project = await projects.find_one({"_id": new_result.inserted_id})
    if project:
        return project
    raise Exception("Project cannot be created")


async def get_project_by_id(project_id: str):
    """A function for fetching a project from the database"""
    project = await projects.find_one({"_id": project_id})
    if project:
        return project
    raise Exception("Project not found")


async def get_all_project(page_number: int, page_size: int):
    """A function for fetching all projects in the database"""
    skip_count = (page_number - 1) * page_size
    all_project = projects.find().skip(skip_count).limit(page_size)
    result = await all_project.to_list(length=page_size)
    return result


async def update_project(project: dict):
    """A function for updating a project"""
    db_project = await projects.find_one({"_id": project["_id"]})
    if db_project:
        for key, value in project.items():
            if value == "" or value == None:
                project[key] = db_project[key]
        await projects.update_one({"_id": project["_id"]}, {"$set": project})
        project = await projects.find_one({"_id": project["_id"]})
        return project
    raise Exception("Project not found")


async def update_project_bugs(project_id: str, bug_id: str):
    """A function for updating the bugs list of a project"""
    project = await get_project_by_id(project_id)
    if project:
        project["bugs"].append(bug_id)
        project = await update_project(project)
        return
    raise Exception("Project does not exist")


async def delete_project(project_id: str):
    """A function for deleting a project"""
    pass


def generate_pagination_query(query, sort=None, next_key=None):
    sort_field = None if sort is None else sort[0]

    def next_key_fn(items):
        if len(items) == 0:
            return None
        item = items[-1]
        if sort_field is None:
            return {"_id": item["_id"]}
        else:
            return {"_id": item["_id"], sort_field: item[sort_field]}

    if next_key is None:
        return query, next_key_fn

    paginated_query = query.copy()

    if sort is None:
        paginated_query["_id"] = {"$gt": next_key["_id"]}
        return paginated_query, next_key_fn

    sort_operator = "$gt" if sort[1] == 1 else "$lt"

    pagination_query = [
        {sort_field: {sort_operator: next_key[sort_field]}},
        {
            "$and": [
                {sort_field: next_key[sort_field]},
                {"_id": {sort_operator: next_key["_id"]}},
            ]
        },
    ]

    if "$or" not in paginated_query:
        paginated_query["$or"] = pagination_query
    else:
        paginated_query = {"$and": [query, {"$or": pagination_query}]}

    return paginated_query, next_key_fn
