"""
Main file to run the Kawaii API.

-- Author: Xayz
-- Version: V1
-- Database: Async PostgreSQL
"""


from __future__ import annotations

import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager

from api.crud import init_db
from api.logger_setup import setup_logging
from api.v1.routes.routes import anime_route
from api.error import register_handler
from api.middleware import register_middleware

version = "v1"

# set-up the logging for the app
setup_logging()

log = logging.getLogger(__name__)

@asynccontextmanager
async def life_span(app: FastAPI):
    log.info(f"Server is starting with API version: {version}....")
    await init_db()
    yield
    log.info("Server has been stopped.")

app = FastAPI(
    title="Kawaii", 
    description="A REST API to get Anime details!", 
    version=version,
    lifespan=life_span
)
app.include_router(anime_route, prefix=f"/api/{version}/anime", tags=["anime"])
register_handler(app=app)
register_middleware(app=app)
