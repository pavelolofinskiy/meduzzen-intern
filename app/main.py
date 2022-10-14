from fastapi import FastAPI
from db import database_pg
from db import database_rd

url_redis = 'redis://:password@hostname:port/0'


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database_pg.connect()


@app.on_event("startup")
async def startup():
    await database_rd.connect()
