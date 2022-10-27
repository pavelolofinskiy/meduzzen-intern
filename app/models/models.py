from sqlalchemy import Integer, String, Column, Table
from sqlalchemy.ext.declarative import declarative_base
from app.database.db import metadata

Base = declarative_base()

users = Table(
    'users',
    metadata,
    Column('username', String, index=True),
    Column('password', String),
    Column('id', Integer, primary_key=True, index=True),
    Column('email', String, index=True),
)



