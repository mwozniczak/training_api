import random

from fastapi import APIRouter

from ..models import Post
from ..fakes import PostFactory

post_routes = APIRouter()

@post_routes.get("/{post_slug}")
async def get_post(post_slug: str) -> Post:
    """
    Retrieves a specific post, using the post's slug (slugs-look-like-this)
    """
    return PostFactory.build(post_uri=f"/posts/{post_slug}")

@post_routes.get("/by_user/{user_id}")
async def get_posts_by_user(user_id: int) -> list[str]:
    """
    Retrieves all posts by a specific user, identified by their numeric user ID
    """
    return [
        PostFactory.post_uri()
        for _ in range(random.randint(0, 10))
    ]