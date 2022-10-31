from sqlalchemy import Integer, String, Column, Table
from app.database.db import metadata

users = Table(
    'users',
    metadata,
    Column('username', String, index=True),
    Column('password', String),
    Column('id', Integer, primary_key=True, index=True),
    Column('email', String, index=True),
)



