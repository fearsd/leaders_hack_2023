from fastapi import FastAPI
from wrapper import run

app = FastAPI()


@app.get('/')
def index() -> str:
    return run()
