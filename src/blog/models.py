from pydantic import BaseModel, Field
from beanie import Document, Link
from datetime import datetime
from typing import List, Optional


class UserSchema(BaseModel):
    name: str
    email: str


class User(UserSchema, Document):

    class Settings:
        collection = "users"


class CommentSchema(BaseModel):
    author: Link[User]
    text: str
    date: datetime = Field(default_factory=datetime.now())


class PostSchema(BaseModel):
    author: Link[User]
    text: str
    date: datetime = Field(default_factory=datetime.now())
    comments: Optional[List[CommentSchema]] = []


class Post(PostSchema, Document):
    class Settings:
        collection = "posts"
