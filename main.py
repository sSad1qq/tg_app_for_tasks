from contextlib import asynccontextmanager

from pydantic import BaseModel
from fastapi import  FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import init_db
import req as rq


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    print('Bot is ready')
    yield


app = FastAPI(title="To Do App", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/tasks/{tg_id}")
async def get_task(tg_id: int):
    user = await rq.add_user(tg_id)
    return await rq.get_tasks(user.id)


@app.get("/api/users/{tg_id}")
async def profile(tg_id: int):
    user = await rq.add_user(tg_id)
    completed_completed_tasks_cnt = await rq.get_completed_tasks_cnt(user.id)
    return {'CompletedTasks': completed_completed_tasks_cnt}