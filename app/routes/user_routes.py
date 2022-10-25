from app.database.db import postgres_engine
from fastapi import FastAPI, Depends
from sqlalchemy.future import select
from app.database.db import SessionLocal
from fastapi import APIRouter
from app.shemas.schemas import UserCreateSchema


router = APIRouter()
app = FastAPI






