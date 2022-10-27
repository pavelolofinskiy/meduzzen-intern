from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import os
from aioredis import from_url
import databases


POSTGRES_USER = os.environ.get('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'postgres')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
POSTGRES_DB = os.environ.get('POSTGRES_DB', 'default_database')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT', 5432)

REDIS_USER = os.environ.get('REDIS_USER', 'redis')
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', 'redis')
REDIS_HOST = os.environ.get('redis_host', 'redis')
REDIS_DB = os.environ.get('REDIS_DB', 'db')


POSTGRES_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
redis_engine = from_url(f'redis://{REDIS_HOST}/{REDIS_DB}', username=REDIS_USER, password=REDIS_PASSWORD)

postgres_engine = create_engine(POSTGRES_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=postgres_engine)

postgres_db = databases.Database(POSTGRES_URL)

metadata = MetaData()

