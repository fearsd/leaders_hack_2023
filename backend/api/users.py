from datetime import date
from typing import List, Optional

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel


from db.db import get_db
from db.models import UserAccount, Attendance, UserBase


class UserDetail(UserBase):
    id: int
    attendances: List[Attendance]


class CheckUserResponse(BaseModel):
    exists: bool
    user: Optional[UserDetail]


class UserListResponse(BaseModel):
    skip: int
    limit: int
    count: int
    users: List[UserAccount]


class HTTPError(BaseModel):
    detail: str

    class Config:
        schema_extra = {
            "example": {"detail": "User not found"},
        }




users_router = APIRouter()


@users_router.get(
    '/check',
    response_model=CheckUserResponse,
    name='Проверка',
    description='Проверка, состоит ли пользователь в проекте "Московское долголетие"'
)
def check(fullname: str, birthday: date, db: Session = Depends(get_db)):
    user = db.query(UserAccount).filter_by(birthday=birthday, fullname=fullname).first()
    return {
        'exists': True if user else False,
        'user': user
    }


@users_router.get(
    '/users/{id}',
    response_model=UserDetail,
    name='Пользователь',
    description='Получение пользователя по id',
    responses={
        status.HTTP_404_NOT_FOUND: {'model': HTTPError} 
    }
)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(UserAccount).get(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@users_router.get(
    '/users',
    response_model=UserListResponse,
    name='Пользователи',
    description='Получение пользователей'
)
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(UserAccount).limit(limit).offset(skip).all()
    count = len(users)
    return {
        'skip': skip,
        'limit': limit,
        'count': count,
        'users': users
    }
