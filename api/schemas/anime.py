from sqlmodel import SQLModel, Field
from typing import Optional


class Anime(SQLModel, table=True):
    __tablename__ = "anime"

    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    title: Optional[str] = Field(default=None, max_length=255)
    synonyms: Optional[str] = Field(default=None)
    japanese: Optional[str] = Field(default=None, max_length=255)
    english: Optional[str] = Field(default=None, max_length=255)
    synopsis: Optional[str] = Field(default=None)
    type: Optional[str] = Field(default=None, max_length=50)
    episodes: Optional[int] = Field(default=None)
    status: Optional[str] = Field(default=None, max_length=50)
    start_aired: Optional[str] = Field(default=None)
    end_aired: Optional[str] = Field(default=None)
    premiered: Optional[str] = Field(default=None, max_length=50)
    broadcast: Optional[str] = Field(default=None, max_length=50)
    producers: Optional[str] = Field(default=None)
    licensors: Optional[str] = Field(default=None)
    studios: Optional[str] = Field(default=None)
    source: Optional[str] = Field(default=None, max_length=50)
    genres: Optional[str] = Field(default=None)
    themes: Optional[str] = Field(default=None)
    demographics: Optional[str] = Field(default=None)
    duration_minutes: Optional[int] = Field(default=None)
    rating: Optional[str] = Field(default=None, max_length=50)
    score: Optional[float] = Field(default=None)
    scored_users: Optional[int] = Field(default=None)
    ranked: Optional[int] = Field(default=None)
    popularity: Optional[int] = Field(default=None)
    members: Optional[int] = Field(default=None)
    favorites: Optional[int] = Field(default=None)


