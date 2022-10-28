from fastapi import FastAPI
from app.routes import user_routes
from app.database.db import postgres_db


app = FastAPI()

app.include_router(user_routes.router)


@app.on_event("startup")
async def startup():
    await postgres_db.connect()


@app.on_event("shutdown")
async def startup():
    await postgres_db.disconnect()