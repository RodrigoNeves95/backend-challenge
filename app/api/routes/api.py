from fastapi import APIRouter
from api.routes import counter

router = APIRouter()
router.include_router(counter.router)
