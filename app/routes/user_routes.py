from fastapi import FastAPI
from app.database.db import postgres_engine, postgres_db, get_db, Session
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

@router.get('/{id}')
async def get_users():
    return await UserCrud.get_users()


@router.post('/user', response_model=ResponseUserId)
async def create(user: UserCreate):
    return await UserCrud.create_user(user=user)


@router.delete('/{id}')
async def destroy(id: int, db: Session = Depends(get_db)):
    return await UserCrud.delete(id, db)


@router.put('/{id}')
async def update(id: int, request: UserUpdate, db: Session = Depends(get_db)):
    return await UserCrud.update_user(id, request, db)

@router.get('/{id}')
async def get_by_id(id: int):
    return await UserCrud.get_by_id(id=id)
