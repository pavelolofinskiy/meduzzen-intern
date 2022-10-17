from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    user = Column('username', String, primary_key=True, index=True)
    password = Column('password', String)
    id = Column('id', Integer, primary_key=True, index=True)
    email = Column('email', String, primary_key=True, index=True)
