from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import date

# User schemas
class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

# Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None

# Contact schemas
class ContactBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    birthday: Optional[date] = None

class ContactCreate(ContactBase):
    pass

class ContactUpdate(ContactBase):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    birthday: Optional[date] = None

class Contact(ContactBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
