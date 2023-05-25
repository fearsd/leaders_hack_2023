from fastapi import FastAPI
from fastapi import APIRouter

from db.db import init_db
from db.models import Category

app = FastAPI(title='LeadersHack 2023 #19track MISIS 5+1')

common_router = APIRouter()

# @app.on_event("startup")
# async def on_startup():
#     init_db()

@common_router.get("/")
async def index():
    return "Everything is ok"


app.include_router(common_router, tags=['common'])
