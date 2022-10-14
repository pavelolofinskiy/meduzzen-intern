from fastapi import FastAPI
from my_datab.db import postgres_db, redis_pool


app = FastAPI()


@app.on_event("startup")
async def startup():
    app.state.redis = await redis_pool()
    await postgres_db.connect()


startup()



