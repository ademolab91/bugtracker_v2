import pprint
from backend import client
from backend.projects import projects
from backend.projects.schemas import ProjectIn
from backend.projects.models import Project
from backend.projects.utils import create_project, generate_pagination_query, get_all_project


async def do_insert(project: ProjectIn):
    return await create_project(project)
    # print(project)


async def do_find_many():
    cursor = projects.find({})
    for project in await cursor.to_list(length=10):
        pprint.pprint(project)


if __name__ == "__main__":
    loop = client.get_io_loop()
    # result1 = loop.run_until_complete(
    #     do_insert(
    #         {
    #             "name": "Bug Tracker",
    #             "description": "An app that help teams keep track of bugs",
    #         }
    #     )
    # )
    # result2 = loop.run_until_complete(
    #     do_insert(
    #         {
    #             "name": "Trek With Me",
    #             "description": "An app that helps users find others to trek with",
    #         }
    #     )
    # )


    # query = {}
    # sort = ["updated_at"]
    # limit = 1
    # query, next_key_fn = generate_pagination_query(query, sort)
    # all_projects = list(projects.find(query).limit(limit).sort([sort]))
    # pprint.pprint(all_projects)
    # next_key = next_key_fn(all_projects)
    # query, next_key_fn = generate_pagination_query(query, sort, next_key)
    # all_projects = list(projects.find(query).limit(limit).sort([sort]))
    # pprint.pprint(all_projects)


    loop.run_until_complete(do_find_many())
    # loop.run_until_complete(
    #     do_insert(
    #         {
    #             "name": "Bug Tracker",
    #             "description": "An app that help teams keep track of bugs",
    #         }
    #     )
    # )
    # p = loop.run_until_complete(get_all_project(3, 1))
    # pprint.pprint(p)
