import asyncio
import datetime
import random

from fastapi import APIRouter, WebSocket

from ..models import SomeKindOfNotification
from ..fakes import (
    NewPostNotificationFactory,
    CommentLikeNotificationFactory,
    PostLikeNotificationFactory,
)

notification_routes = APIRouter()

def _make_notification(read_status: bool|None = None, now: bool = False) -> SomeKindOfNotification:
    func = random.choice(
        (NewPostNotificationFactory, CommentLikeNotificationFactory, PostLikeNotificationFactory)
    ).build
    kwargs = {}
    if read_status is not None:
        kwargs["is_read"] = read_status
    if now:
        kwargs["timestamp"] = datetime.datetime.now()
    return func(**kwargs)

@notification_routes.get("/")
async def list_notifications() -> list[SomeKindOfNotification]:
    """
    Retrieves a list of recent notifications, sorted by whether they've been read.
    """
    return sorted([
        _make_notification()
        for _ in range(random.randint(5, 20))
    ], key=lambda x: (x.is_read, x.timestamp))

@notification_routes.websocket("/feed")
async def live_feed(ws: WebSocket):
    """
    Live updates for notifications
    """
    await ws.accept()
    try:
        while True:
            await ws.send_text(_make_notification(False, True).model_dump_json())
            await asyncio.sleep(random.randrange(2.0, 10))
    except:
        pass