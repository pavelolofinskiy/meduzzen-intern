import databases
from os import getenv
import redis


async def redis_pool() -> redis.Redis:
    my_redis = redis.from_url(
        f'redis://rd_database',
        encoding='utf-8',
        db=0,
        decode_responses=True,
    )
    return my_redis

POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = 'postgres'
POSTGRES_HOST = 'postgres'
POSTGRES_DB = 'default_database'
POSTGRES_PORT = 5432

POSTGRES_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
postgres_db = databases.Database(POSTGRES_URL)




