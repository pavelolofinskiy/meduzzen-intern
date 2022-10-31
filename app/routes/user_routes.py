from app.database.db import postgres_engine
from app.models.models import users as DBUser
from app.shemas.schemas import UserCreate, ResponseUserId, UserUpdate, PublicUser, Users
from app.services.services import UserCrud
from fastapi import APIRouter

router = APIRouter()


@router.get('/', status_code=200)
async def root():
    return {'status':'Working!', 'postgres': postgres_engine.__str__()}


@router.post('/user', response_model=ResponseUserId)
async def create(user: UserCreate) -> ResponseUserId:
    crud = UserCrud(db_user=DBUser)
    return await crud.create_user(user=user)


@router.delete('/{id}', response_model=ResponseUserId)
async def destroy(id: int) -> ResponseUserId:
    crud = UserCrud(db_user=DBUser)
    return await crud.delete_user(id=id)


@router.put('/{id}', response_model=ResponseUserId)
async def update(id: int, user_in: UserUpdate) -> ResponseUserId:
    crud = UserCrud(db_user=DBUser)
    return await crud.update_user(id=id, user_in=user_in)


@router.get('/users', response_model=Users)
async def get_users() -> Users:
    crud = UserCrud(db_user=DBUser)
    user = await crud.get_users()
    return user


@router.get('/{id}', response_model=PublicUser)
async def get_by_id(id: int) -> PublicUser:
    crud = UserCrud(db_user=DBUser)
    user = await crud.get_by_id(id=id)
    return user
