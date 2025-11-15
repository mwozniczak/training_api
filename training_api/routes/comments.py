from fastapi import APIRouter

from ..models import Comment
from ..fakes import CommentFactory
from ..utils.flakiness import flaky, slow

comment_routes = APIRouter()

@comment_routes.get("/{comment_id}")
@flaky()
@slow(odds=1)
async def get_specific_comment(comment_id: str) -> Comment:
    return CommentFactory.build(comment_id=comment_id)