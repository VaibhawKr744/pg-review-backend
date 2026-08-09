from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class PGCreate(BaseModel):
    name: str
    city: str
    address: str


class PGOut(BaseModel):
    id: int
    name: str
    city: str
    address: str
    created_at: datetime

    class Config:
        from_attributes = True


class ReviewCreate(BaseModel):
    rating: int
    deposit_returned: bool
    comment: str | None = None


class ReviewOut(BaseModel):
    id: int
    user_id: int
    pg_id: int
    rating: int
    deposit_returned: bool
    comment: str | None
    created_at: datetime

    class Config:
        from_attributes = True
