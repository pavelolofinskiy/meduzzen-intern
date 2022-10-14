import databases

POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = 'postgres'
POSTGRES_HOST = 'postgres'
POSTGRES_DB = 'default_database'
POSTGRES_PORT = 5432

POSTGRES_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
database_pg = databases.Database(POSTGRES_URL)

REDIS_USER = 'redis'
REDIS_PASSWORD = 'password'
REDIS_HOST = 'redis'
REDIS_PORT = 6379
REDIS_DB = 'default_database'

url_redis = f'redis://{REDIS_USER}:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'
database_rd = databases.Database(url_redis)