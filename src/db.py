from .config import DatabaseSettings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from .blog.models import *


async def init_db():
    db_configs = DatabaseSettings()
    client = AsyncIOMotorClient(f"mongodb://{db_configs.user}:{db_configs.password}@{db_configs.host}:{db_configs.port}")
    await init_beanie(database=client.Blog, document_models=[User, Post])