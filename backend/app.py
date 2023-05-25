from fastapi import FastAPI
from fastapi import APIRouter

app = FastAPI(title='LeadersHack 2023 #19track MISIS 5+1')

common_router = APIRouter()

@common_router.get("/")
async def index():
    return "Everything is ok"


app.include_router(common_router, tags=['common'])
