from beanie.odm.fields import PydanticObjectId
from fastapi import APIRouter
from .models import User, UserSchema, PostSchema, Post
from typing import List

users_router = APIRouter(prefix="/users", tags=["users"])
posts_router = APIRouter(prefix="/posts", tags=["posts"])


@users_router.get("/")
async def list_users() -> List[User]:
    users = await User.find().to_list()
    return users


@users_router.get("/{user_id}")
async def retrieve_user(user_id: PydanticObjectId) -> User:
    user = await User.get(user_id)
    return user


@users_router.post("/")
async def create_user(user: UserSchema) -> User:
    db_user = await User.parse_obj(user).insert()
    return db_user


@users_router.delete("/{user_id}")
async def delete_user(user_id: PydanticObjectId) -> None:
    user = await User.get(user_id)
    await user.delete()


@posts_router.get("/")
async def list_posts() -> List[Post]:
    return await Post.find().to_list()


@posts_router.get("/{post_id}")
async def retrieve_post(post_id: int) -> Post:
    return await Post.get(post_id)


@posts_router.post("/")
async def create_post(post: PostSchema) -> Post:
    print(post)