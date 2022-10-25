import fastapi
import uvicorn
from fastapi import FastAPI, APIRouter
from app.database.db import postgres_engine, postgres_db
from app.shemas.schemas import UserCreateSchema
from app.routes import user_routes
import sqlalchemy.orm as orm
from app.services import services


app = FastAPI()


@app.on_event("startup")
async def startup():
    await postgres_db.connect()


@app.get('/', status_code=200)
async def root():
    return {'status':'Working!', 'postgres': postgres_engine.__str__()}


@app.post('/user')
async def create(request: UserCreateSchema, db: orm.Session = fastapi.Depends(services.get_db)):
    return await services.create_user(request=request, db=db)



