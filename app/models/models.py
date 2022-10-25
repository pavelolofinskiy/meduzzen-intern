from sqlalchemy import Integer, String, Column, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    username = Column('username', String, index=True)
    password = Column('password', String)
    id = Column('id', Integer, primary_key=True, index=True)
    email = Column('email', String, index=True)


users = User.__table__
