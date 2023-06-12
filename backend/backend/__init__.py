import motor.motor_asyncio as mt_async
from .config import Settings


settings = Settings()
client = mt_async.AsyncIOMotorClient(settings.database_url)
db = client.bug_tracker
