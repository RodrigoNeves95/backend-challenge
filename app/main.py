import uvicorn
from fastapi import FastAPI
from api.routes.api import router

from core.config import API_PREFIX, PROJECT_NAME, VERSION, DEBUG
from starlette_prometheus import metrics, PrometheusMiddleware


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
    application.include_router(router, prefix=API_PREFIX)
    return application


app = get_application()
# Add middleware with metrics for our server for Prometheus.
# On this metrics is included number of unique IP adress. All the other
# are just out of the scope, but it's also good to have it.
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", metrics)

if __name__ == "__main__":
    # Start server with reload and debug active for development purposes.
    # Setup production ready deployment is out of the scope
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True, debug=True)
