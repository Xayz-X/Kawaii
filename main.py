from __future__ import annotations

from fastapi import FastAPI
from contextlib import asynccontextmanager
from api.crud.db import init_db
from api.v1.routes.routes import anime_route


@asynccontextmanager
async def life_span(app: FastAPI):
    print("Server is starting....")
    await init_db()
    yield
    print("Server has been stopped")


version = "v1"

app = FastAPI(
    title="Kawaii", 
    description="A REST API to get Anime details!", 
    version=version,
    lifespan=life_span
)

app.include_router(anime_route, prefix=f"/api/{version}/anime", tags=["anime"])


