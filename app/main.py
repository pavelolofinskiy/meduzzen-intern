from fastapi import FastAPI
import databases


DATABASE_URL = 'postgresql://postgres:postgres@127.0.0.1:5432/default_database'

postgres_db = databases.Database(DATABASE_URL)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await postgres_db.connect()




