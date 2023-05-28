from datetime import date
from typing import List, Optional

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel

from db.db import get_db
from db.poll_models import (Poll, PollBase, QuestionBase, Option, Result, Answer)

polls_router = APIRouter()

class QuestionDetail(QuestionBase):
    id: int
    options: List[Option]

class PollDetail(PollBase):
    id: int
    questions: List[QuestionDetail]


@polls_router.get(
    '/poll',
    response_model=PollDetail,
    name='Опрос',
    description='Получение актуального опроса'
)
def get_poll(db: Session = Depends(get_db)):
    return db.query(Poll).first()
