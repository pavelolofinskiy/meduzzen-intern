import databases
from os import getenv
import redis


async def redis_pool() -> redis.Redis:
    my_redis = redis.from_url(
        'redis://rd_database',
        encoding='utf-8',
        db=0,
        decode_responses=True,
    )
    return my_redis


POSTGRES_URL = f'postgresql://{getenv("POSTGRES_USER")}:{getenv("POSTGRES_PASSWORD")}@{getenv("POSTGRES_HOST")}:{getenv("POSTGRES_PORT")}/{getenv("POSTGRES_DB")}'
database_pg = databases.Database(POSTGRES_URL)

client = redis.Redis(host=getenv('REDIS_HOST'))
