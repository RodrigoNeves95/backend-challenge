from fastapi import APIRouter, HTTPException, status
from services.counter import CustomIPCounter
from prometheus_client.core import CounterMetricFamily, REGISTRY

from loguru import logger
import os

router = APIRouter()
counter = CustomIPCounter()

REGISTRY.register(counter)

@router.post("/logs")
async def ip_post_request(payload : dict):
    try:
        counter.register(payload)
    except Exception as e:
        logger.debug(e)
        # ToDo: Better error handling should be in place
        return status.HTTP_400_BAD_REQUEST
    return status.HTTP_200_OK


#@router.get("/metrics")
#async def ip_post_request() -> int:
#    logger.debug(counter.ips)
#    return len(list(set(counter.ips)))

