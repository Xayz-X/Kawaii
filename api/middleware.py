import time
import logging

from fastapi import FastAPI
from fastapi.requests import Request

log = logging.getLogger(__name__)


def register_middleware(app: FastAPI):

    @app.middleware("http")
    async def custom_logging(request: Request, call_next):
        start_time = time.time()

        response = await call_next(request)

        duration = time.time() - start_time
        msg = f"{request.client.host}:{request.client.port} -> {request.method} | {request.url.path} | {response.status_code} -> {duration:.4f}"
        log.info(msg)
        return response
