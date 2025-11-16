from fastapi import APIRouter

from ..models import Comment
from ..fakes import CommentFactory
from ..utils.flakiness import flaky, slow

comment_routes = APIRouter()

@comment_routes.get("/{comment_id}")
@flaky(odds=.5)
@slow(odds=.5)
async def get_specific_comment(comment_id: str) -> Comment:
    """
    Retrieves a specific comment, based on the comment's UUID

    Note, that since this is an "integration" with an "external" service that "exists",
    it can be notoriously flaky, slow, and overall garbage! It frequently errors out,
    is slow to respond sometimes, you get the idea.
    """
    return CommentFactory.build(comment_id=comment_id)