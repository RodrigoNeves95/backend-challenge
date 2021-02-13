import socket
import uvicorn
from fastapi import FastAPI
from api.routes.api import router
import threading
from http.server import HTTPServer
from core.config import API_PREFIX, PROJECT_NAME, VERSION, DEBUG
from prometheus_client import MetricsHandler

from loguru import logger

# main.py
from concurrent.futures import ThreadPoolExecutor
import asyncio


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
    application.include_router(router, prefix=API_PREFIX)
    return application


PROMETHEUS_PORT = 9012


class PrometheusEndpointServer(threading.Thread):
    """A thread class that holds an http and makes it serve_forever()."""

    def __init__(self, httpd, *args, **kwargs):
        self.httpd = httpd
        super(PrometheusEndpointServer, self).__init__(*args, **kwargs)

    def run(self):
        self.httpd.serve_forever()


def start_prometheus_server():
    try:
        httpd = HTTPServer(("0.0.0.0", PROMETHEUS_PORT), MetricsHandler)
    except (OSError, socket.error):
        return

    thread = PrometheusEndpointServer(httpd)
    thread.daemon = True
    thread.start()
    logger.info(
        f"Exporting Prometheus /metrics/ on port {PROMETHEUS_PORT}",
    )


app = get_application()

if __name__ == "__main__":
    # Start server with reload and debug active for development purposes.
    start_prometheus_server()
    # Setup production ready deployment is out of the scope
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True, debug=True)
