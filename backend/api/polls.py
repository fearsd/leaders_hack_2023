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


class AnswerPost(BaseModel):
    question_id: int
    options: List[int]


class ResultPost(BaseModel):
    poll_id: int
    answers: List[AnswerPost]


@polls_router.get(
    '/poll',
    response_model=PollDetail,
    name='Опрос',
    description='Получение актуального опроса'
)
def get_poll(db: Session = Depends(get_db)):
    return db.query(Poll).first()


@polls_router.post(
    '/polls/result',
    name='Результат',
    description='Сохранение результатов опроса',
    response_model=Result
)
def post_result(result: ResultPost, db: Session = Depends(get_db)):
    result = result.dict()
    answers = result.pop('answers', None)
    res = Result(**result)
    db.add(res)
    db.commit()
    db.refresh(res)
    for ans in answers:
        ans['result_id'] = res.id
        ans['options'] = [db.query(Option).get(id) for id in ans['options']]
        _ans = Answer(**ans)
        db.add(_ans)
        db.commit()

    # db.bulk_insert_mappings(Answer, answers)
    # db.commit()
    db.refresh(res)
    return res
