import uvicorn
from fastapi import FastAPI
from api.routes.api import router

from core.config import API_PREFIX, PROJECT_NAME, VERSION, DEBUG


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
    application.include_router(router, prefix=API_PREFIX)
    return application


app = get_application()


if __name__ == "__main__":
    # Start server with reload and debug active for development purposes.
    # Setup production ready deployment is out of the scope
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True, debug=True)
