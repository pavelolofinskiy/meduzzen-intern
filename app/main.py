from fastapi import FastAPI
from app.database.db import postgres_engine, postgres_db, get_db
from app.shemas.schemas import UserCreateSchema, ResponseUserId
from app.services.services import UserCrud
from typing import List

app = FastAPI()


@app.on_event("startup")
async def startup():
    await postgres_db.connect()


@app.on_event("shutdown")
async def startup():
    await postgres_db.disconnect()


@app.get('/', status_code=200)
async def root():
    return {'status':'Working!', 'postgres': postgres_engine.__str__()}


@app.post('/user', response_model=ResponseUserId)
async def create(user: UserCreateSchema):
    return await UserCrud.create_user(user=user)


@app.get("/users/", response_model=List[ResponseUserId])
async def read_users():
    return await UserCrud().get_users()


