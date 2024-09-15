from pydantic import BaseModel
from typing import Optional
from api.schemas.anime import Anime


class AnimeModel(BaseModel):
    id: int
    title: str
    synonyms: str
    japanese: str
    english: str
    synopsis: str
    type: str
    episodes: int
    status: str
    start_aired: str
    end_aired: str
    premiered: str
    broadcast: str
    producers: str
    licensors: str
    studios: str
    source: str
    genres: str
    themes: str
    demographics: str
    duration_minutes: int
    rating: str
    score: float
    scored_users: int
    ranked: int
    popularity: int
    members: int
    favorites: int

    class Config:
        from_attributes = True
        