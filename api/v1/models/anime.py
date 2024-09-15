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
        
        
def convert_to_anime_model(anime: Anime) -> AnimeModel:
    return AnimeModel(
        id=anime.id,
        title=anime.title,
        synonyms=anime.synonyms,
        japanese=anime.japanese,
        english=anime.english,
        synopsis=anime.synopsis,
        type=anime.type,
        episodes=anime.episodes,
        status=anime.status,
        start_aired=anime.start_aired,
        end_aired=anime.end_aired,
        premiered=anime.premiered,
        broadcast=anime.broadcast,
        producers=anime.producers,
        licensors=anime.licensors,
        studios=anime.studios,
        source=anime.source,
        genres=anime.genres,
        themes=anime.themes,
        demographics=anime.demographics,
        duration_minutes=anime.duration_minutes,
        rating=anime.rating,
        score=anime.score,
        scored_users=anime.scored_users,
        ranked=anime.ranked,
        popularity=anime.popularity,
        members=anime.members,
        favorites=anime.favorites,
    )
