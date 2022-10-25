from app.database.db import postgres_db, Session
from app.shemas.schemas import UserCreateSchema
from app.models.models import users
from fastapi import HTTPException, status



class UserCrud:
    @staticmethod
    async def create_user(user: UserCreateSchema):
        db_user = users.insert().values(email=user.email, username=user.username, password=user.password)
        user_id = await postgres_db.execute(db_user)
        if user_id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'user with id {user_id} already exists')
        return dict(**user.dict(), id=user_id)

    @staticmethod
    async def get_users():
        results = await postgres_db.fetch_all(users.select())
        return [dict(result) for result in results]



    @staticmethod
    async def edit_user():
        results = await postgres_db.fetch_all(users.select())
