from app.database.db import postgres_db, Session
from app.shemas.schemas import UserUpdate, UserCreate
from app.models.models import my_users, User
from fastapi import HTTPException, status


class UserCrud:
    @staticmethod
    async def create_user(user: UserCreate):
        db_user = my_users.insert().values(email=user.email, username=user.username, password=user.password)
        user_id = await postgres_db.execute(db_user)
        if user_id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'user with id {user_id} already exists')
        return dict(**user.dict(), id=user_id)

    @staticmethod
    async def get_users():
        results = await postgres_db.fetch_all(my_users.select())
        return [dict(result) for result in results]

    @staticmethod
    async def get_by_id(id: int, db: Session):
        user = db.query(User).filter(User.id == id).first
        return user

    @staticmethod
    async def update_user(id: int, request: UserUpdate, db: Session):
        user = db.query(User).filter(User.id == id)
        items = dict(password=request.password, username=request.username)
        if not user.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"User with id {id} not found")
        user.update(items)
        db.commit()
        return 'update'

    @staticmethod
    async def delete(id: int, db: Session):
        user = db.query(User).filter(User.id == id)
        if not user.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"User with id {id} not found")
        user.delete()
        db.commit()
        return 'done'


