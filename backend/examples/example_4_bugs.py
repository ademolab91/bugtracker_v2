from pprint import pprint
from backend.bugs.utils import create_bug, get_bug, get_all_bug, get_all_bug_in_a_project, update_bug
from backend import client


async def main():
    bug1 = await update_bug(
        {
            "_id": "168a2ebd-745d-499d-855a-d7cbf16aa19f",
            "title": "The kinikan have not been tested",
            "description": "The fact that the utilities have not been tested might result in an unforeseen error, they must be tested as soon as possible",
            # "project_id": "ed4a8a08-a05b-4fb2-81d0-d9fc1c387cc7",
        }
    )
    pprint(bug1)
    # pprint(await get_all_bug_in_a_project("ed4a8a08-a05b-4fb2-81d0-d9fc1c387cc7", 1, 10))


if __name__ == "__main__":
    loop = client.get_io_loop()
    loop.run_until_complete(main())
