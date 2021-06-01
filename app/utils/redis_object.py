from app.utils.const import TESTING, TEST_REDIS_URL
import aioredis

redis = None

async def check_redis_status():
    global redis
    if TESTING:
        redis = await aioredis.create_redis_pool(TEST_REDIS_URL)
