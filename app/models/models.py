from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    user = Column('user_id', String, primary_key=True, index=True)
    password = Column('user_id', String)
    id = Column('user_id', Integer, primary_key=True, index=True)
    email = Column('user_id', String, primary_key=True, index=True)
