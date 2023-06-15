from fastapi import FastAPI
from .db import init_db
from .blog.models import User
from .blog.views import users_router, posts_router

app = FastAPI()
app.include_router(users_router)
app.include_router(posts_router)


@app.on_event("startup")
async def start_db():
    await init_db()


@app.post("/")
async def read_root(user: User):
    await user.insert()
    return {"Hello": "World"}