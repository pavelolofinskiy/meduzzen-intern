from fastapi import FastAPI
from my_datab import db
from my_datab import db


app = FastAPI()


@app.on_event("startup")
async def startup():
    app.state.redis = await db.redis_pool()

startup()



