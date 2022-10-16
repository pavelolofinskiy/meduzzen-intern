#from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import databases
import os
import redis
from aioredis import from_url

async def redis_pool() -> redis.Redis:
    my_redis = redis.from_url(
        f'redis://rd_database',
        encoding='utf-8',
        db=0,
        decode_responses=True,
    )
    return my_redis

POSTGRES_USER = os.environ.get('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'postgres')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'postgres')
POSTGRES_DB = os.environ.get('POSTGRES_DB', 'default_database')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT', 5432)

REDIS_USER = os.environ.get('REDIS_USER', 'redis')
REDIS_DB = os.environ.get('REDIS_DB', 'db')


#postgres_engine = create_async_engine(f'postgres+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}')
#redis_engine = from_url()

POSTGRES_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
postgres_db = databases.Database(POSTGRES_URL)
print(POSTGRES_URL)



