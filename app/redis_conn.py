import aioredis
from config import settings

REDIS_URL = settings.redis_url

async def create_redis_pool() -> aioredis.Redis:
    redis = await aioredis.from_url(REDIS_URL, encoding="utf-8", decode_responses=True)
    return redis
