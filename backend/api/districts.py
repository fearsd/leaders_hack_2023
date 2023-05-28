from typing import List

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from db.db import get_db
from db.models import District

district_router = APIRouter()


@district_router.get(
    '/districts',
    name='Округа'
)
def get_districts(db: Session = Depends(get_db)) -> List[District]:
    return db.query(District).all()
