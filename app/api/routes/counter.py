from fastapi import APIRouter, HTTPException, status
from services.counter import CustomIPCounter

from loguru import logger

from starlette_prometheus import metrics, PrometheusMiddleware
from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily, REGISTRY

router = APIRouter()
counter = CustomIPCounter()

REGISTRY.register(counter)


@router.post("/logs")
async def ip_post_request(payload: dict):
    try:
        counter.register(payload)
    except Exception as e:
        logger.debug(e)
        # ToDo: Better error handling should be in place
        return status.HTTP_400_BAD_REQUEST
    return status.HTTP_200_OK
