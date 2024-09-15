from typing import List
from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from api.crud.db import get_session
from api.v1.models.anime import AnimeModel

from sqlalchemy.ext.asyncio import AsyncSession
from api.crud.services.service import AnimeService

anime_route = APIRouter()
anime_service: AnimeService = AnimeService()


@anime_route.get("/", status_code=status.HTTP_200_OK)
async def default_route() -> dict:
    return "Anime route is working fine"


@anime_route.get("/{id}", response_model=AnimeModel, status_code=status.HTTP_200_OK)
async def get_single_anime(
    id: int, session: AsyncSession = Depends(get_session)
) -> AnimeModel:
    result = await anime_service.get_specific_anime_by_id(anime_id=id, session=session)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Anime data not found with id {id}",
        )
    return result


@anime_route.get("/count", status_code=status.HTTP_200_OK)
async def get_anime_counts(session: AsyncSession = Depends(get_session)) -> dict:
    result = await anime_service.count_anime_rows(session=session)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Anime data not found",
        )
    return {"total": result}
