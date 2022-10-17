from app.database.db import postgres_engine
from fastapi import FastAPI

app = FastAPI()

@app.get('/', status_code=200)
async def root():
    return {'status':'Working!', 'postgres': postgres_engine.__str__()}
