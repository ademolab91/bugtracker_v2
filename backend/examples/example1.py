import motor.motor_asyncio as mt

client = mt.AsyncIOMotorClient('mongodb://localhost:27017')
db = client.test_database
collection = db.test_collection


async def do_insert():
    result = await collection.insert_one({'x': 1})
    return result.inserted_id


async def do_find_one():
    """Find a single document."""
    document = await collection.find_one({'_id': await do_insert()})
    print('found %s' % document)


if __name__ == '__main__':
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(do_find_one())