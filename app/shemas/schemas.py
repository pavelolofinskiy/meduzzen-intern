from pydantic import BaseModel, EmailStr


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


