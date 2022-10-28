from pydantic import BaseModel, EmailStr
from typing import List


class UserCreate(BaseModel):
    username: str
    password: str
    email: EmailStr

    class Config:
        orm_mode: True


class UserUpdate(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode: True


class ResponseUserId(BaseModel):
    id: int

    class Config:
        orm_mode: True


class PublicUser(BaseModel):
    username: str
    email: EmailStr
    id: int

    class Config:
        orm_mode: True


class Users(BaseModel):
    users: List[PublicUser] = []

