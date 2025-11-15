import asyncio
import random

from fastapi import APIRouter, WebSocket

from ..models import (
    NewPostNotification,
    CommentLikeNotification,
    PostLikeNotification,
)
from ..fakes import (
    NewPostNotificationFactory,
    CommentLikeNotificationFactory,
    PostLikeNotificationFactory,
)

notification_routes = APIRouter()

def make_notification(read_status: bool|None = None) -> NewPostNotification|CommentLikeNotification|PostLikeNotification:
    func = random.choice(
        (NewPostNotificationFactory, CommentLikeNotificationFactory, PostLikeNotificationFactory)
    ).build
    if read_status is None:
        return func()
    return func(is_read=read_status)

@notification_routes.get("/")
async def list_notifications() -> list[NewPostNotification|CommentLikeNotification|PostLikeNotification]:
    return sorted([
        make_notification()
        for _ in range(random.randint(5, 20))
    ], key=lambda x: x.is_read)

@notification_routes.websocket("/feed")
async def live_feed(ws: WebSocket):
    await ws.accept()
    while True:
        await ws.send_text(make_notification(False).model_dump_json())
        await asyncio.sleep(random.randrange(2.0, 10))
