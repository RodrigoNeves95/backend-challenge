from fastapi import APIRouter, HTTPException, status
from services.counter import CustomIPCounter

router = APIRouter()
counter = CustomIPCounter()

@router.post("/logs")
async def ip_post_request(payload : dict):
    try:
        counter.register(payload)
    except:
        # ToDo: Better error handling should be in place
        return status.HTTP_400_BAD_REQUEST
    return status.HTTP_200_OK

