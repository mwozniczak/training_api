from datetime import datetime
from typing import Generic, TypeVar

from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar("T")

class User(BaseModel):
    user_id: int
    user_name: str
    full_name: str
    email: str = Field(example="someone@example.com")
    recent_comments: list[str]

class Post(BaseModel):
    post_uri: str
    post_date: datetime
    user_id: int
    title: str
    body: str


class Comment(BaseModel):
    comment_id: str
    timestamp: datetime
    post_id: int
    author_id: int
    comment: str


class Notification(BaseModel):
    timestamp: datetime
    is_read: bool = False


class NewPostNotification(Notification):
    post_uri: str


class LikeNotification(Notification):
    liked_by: int

class CommentLikeNotification(LikeNotification):
    comment_id: str


class PostLikeNotification(LikeNotification):
    post_uri: str


class RecentNotifications(BaseModel):
    items: list[NewPostNotification|NewPostNotification|CommentLikeNotification]


class PaginatedObject(GenericModel, Generic[T]):
    items: list[T]
    current_page: int = 0
    total_pages: int
