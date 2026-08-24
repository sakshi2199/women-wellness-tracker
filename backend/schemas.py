from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class CycleCreate(BaseModel):
    start_date: date
    end_date: Optional[date] = None

class CycleOut(BaseModel):
    id: int
    user_id: int
    start_date: date
    end_date: Optional[date]

    class Config:
        from_attributes = True