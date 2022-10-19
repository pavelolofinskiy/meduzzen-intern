from app.models.models import User
from app.database.db import SessionLocal, Base, postgres_engine
from app.shemas.schemas import UserCreateSchema, ResponseUserId


async def add_tables():
    return Base.metadata.create_all(bind=postgres_engine)


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def create_user(request: UserCreateSchema, db: 'Session') -> UserCreateSchema:
    user = UserCreateSchema(username=request.username, email=request.email, password=request.password, id=request.id)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


