from datetime import date

from sqlalchemy.orm import Session
from sqlmodel import select
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from db.db import get_db
from db.models import UserAccount


class CheckUserResponse(BaseModel):
    exists: bool


users_router = APIRouter()


@users_router.get('/check', response_model=CheckUserResponse)
def check(fullname: str, birthday: date, db: Session = Depends(get_db)):
    result = db.query(UserAccount).filter_by(birthday=birthday, fullname=fullname).count()
    return {
        'exists': True if result else False
    }
    