from fastapi import FastAPI
from fastapi import APIRouter

from db.models import (Category, Level1, Level2, District, Schedule,
                       Municipal, Address,
                       Route, UserAccount, #Group, Attendance
                       )

app = FastAPI(title='LeadersHack 2023 #19track MISIS 5+1')

common_router = APIRouter()

# @app.on_event("startup")
# async def on_startup():
#     init_db()


@common_router.get("/")
async def index():
    return "Everything is ok"


app.include_router(common_router, tags=['common'])
