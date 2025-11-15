from fastapi import FastAPI

from .routes import *

app = FastAPI(
    title="Fake Social API",
    description="""
    Simulated API that pretends it's for a social media-ish site.
    The purpose of it is to be a teaching aid for exploring more advanced Python ideas,
    such as various forms of multiprocessing, asynchronicity, usage of libraries for
    interacting with remote data (httpx/requests, websockets, retry, etc.)
    """
)
app.include_router(user_routes, prefix="/users")
app.include_router(comment_routes, prefix="/comments")
app.include_router(post_routes, prefix="/posts")
app.include_router(notification_routes, prefix="/notifications")