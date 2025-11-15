from fastapi import APIRouter, Query, HTTPException

from ..models import PaginatedObject, User
from ..fakes import UserFactory
from ..utils.pagination import paginate

user_routes = APIRouter()

TOTAL_USERS = 500

PREGENS = [
    UserFactory.build(user_id=i) for i in range(TOTAL_USERS)
]

@user_routes.get("/")
async def list_all_users(
    page: int = Query(0, ge=0, le=TOTAL_USERS),
    items_per_page: int = Query(20, ge=1, le=100)
) -> PaginatedObject[User]:
    return paginate(
        PREGENS,
        page,
        items_per_page
    )

@user_routes.get("/{user_id}")
async def get_specific_user(user_id: int) -> User:
    if user_id not in range(TOTAL_USERS):
        raise HTTPException(404)
    return PREGENS[user_id]