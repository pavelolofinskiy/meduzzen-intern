from fastapi import FastAPI
from app.database.db import postgres_engine, postgres_db
from app.shemas.schemas import UserCreate, ResponseUserId, UserUpdate
from app.services.services import UserCrud
from typing import List
from fastapi import APIRouter, Depends

router = APIRouter()


@router.on_event("startup")
async def startup():
    await postgres_db.connect()


@router.on_event("shutdown")
async def startup():
    await postgres_db.disconnect()


@router.get('/', status_code=200)
async def root():
    return {'status':'Working!', 'postgres': postgres_engine.__str__()}


@router.post('/user', response_model=ResponseUserId)
async def create(user: UserCreate) -> ResponseUserId:
    return await UserCrud.create_user(user=user)


@router.delete('/{id}', response_model=ResponseUserId)
async def destroy(id: int):
    return await UserCrud.delete(id=id)


@router.put('/{id}', response_model=ResponseUserId)
async def update(id: int, user_in: UserUpdate):
    return await UserCrud.update_user(id=id, user_in=user_in)


@router.get('/{id}', response_model=UserCreate)
async def get_by_id(id: int):
    user = UserCrud.get_by_id(id=id)
    return user