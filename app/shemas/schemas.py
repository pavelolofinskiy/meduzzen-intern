from pydantic import BaseModel, EmailStr, Field


class UserCreateSchema(BaseModel):
    username: str = Field(min_length=6, max_length=24)
    password: str = Field(min_length=6, max_length=24)
    email: EmailStr
    id: int

    class Config:
        orm_mode: True


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=24)

    class Config:
        orm_mode: True


class ResponseUserId(BaseModel):
    id: int
