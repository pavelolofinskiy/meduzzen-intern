from fastapi import FastAPI
from app.db import redis_pool, postgres_db


app = FastAPI()


@app.on_event("startup")
async def startup():
    app.state.redis = await redis_pool()
    await postgres_db.connect()


startup()




