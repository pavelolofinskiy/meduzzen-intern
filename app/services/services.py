from app.database.db import postgres_db
from app.shemas.schemas import UserUpdate, UserCreate, ResponseUserId, PublicUser, Users
from app.models.models import users as DBUser
from fastapi import HTTPException, status


class UserCrud:
    def __init__(self, db_user: DBUser = None):
        self.db_user = db_user

    async def create_user(self, user: UserCreate) -> ResponseUserId:
        db_user = self.db_user.insert().values(email=user.email, username=user.username, password=user.password)
        user_id = await postgres_db.execute(db_user)
        if user_id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'user with id {user_id} already exists')
        return ResponseUserId(id=user_id)

    async def get_users(self) -> Users:
        results = await postgres_db.fetch_all(self.db_user.select())
        users = [PublicUser(result) for result in results]
        return Users(users=users)

    async def get_by_id(self, id: int) -> PublicUser:
        user = await postgres_db.fetch_one(self.db_user.select().where(self.db_user.c.id == id))
        return PublicUser(**user)

    async def update_user(self, id: int, user_in: UserUpdate) -> ResponseUserId:
        updated_data = user_in.dict()
        update = self.db_user.update().values(updated_data).where(self.db_user.c.id == id)
        await postgres_db.execute(update)
        return ResponseUserId(id=id)

    async def delete_user(self, id: int) -> ResponseUserId:
        delete = self.db_user.delete().where(self.db_user.c.id == id)
        await postgres_db.execute(delete)
        return ResponseUserId(id=id)
