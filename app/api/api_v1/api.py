from fastapi import APIRouter

from .endpoints import user#, search



router = APIRouter()

router.include_router(user.router, prefix='/user', tags=['User'])
#router.include_router(search.router, prefix='/search', tags=['Search'])