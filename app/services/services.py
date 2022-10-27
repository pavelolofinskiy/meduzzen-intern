from app.database.db import postgres_db, Session
from app.shemas.schemas import UserUpdate, UserCreate, ResponseUserId
from app.models.models import users as DBUser
from fastapi import HTTPException, status


class UserCrud:
    @staticmethod
    async def create_user(user: UserCreate) -> ResponseUserId:
        db_user = DBUser.insert().values(email=user.email, username=user.username, password=user.password)
        user_id = await postgres_db.execute(db_user)
        if user_id:
            raise HTTPException(403, detail=f'User {user_id} already exist')
        return ResponseUserId(id=user_id)

    @staticmethod
    async def get_users():
        results = await postgres_db.fetch_all(DBUser.select())
        return [dict(result) for result in results]

    @staticmethod
    async def get_by_id(id: int) -> UserCreate:
        user = postgres_db.fetch_one(DBUser.select().where(DBUser.c.id == id))
        return UserCreate(**user)

    @staticmethod
    async def update_user(id: int, user_in: UserUpdate) -> ResponseUserId:
        updated_data = user_in.dict()
        update = DBUser.update().values(updated_data).where(DBUser.c.id == id)
        await postgres_db.execute(update)
        return ResponseUserId(id=id)

    @staticmethod
    async def delete(id: int) -> ResponseUserId:
        delete = DBUser.delete().where(DBUser.c.id == id)
        await postgres_db.execute(delete)
        return ResponseUserId(id=id)


