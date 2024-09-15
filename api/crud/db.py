from __future__ import annotations

from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from api.secrets.config import Config

async_engine: AsyncEngine = create_async_engine(
    url=Config.DATABASE_URL, 
    # echo=True,
    # pool_size=5,
    # max_overflow=10,
    # pool_recycle=3600  
    )

async def init_db():
    async with async_engine.begin() as con:
        from api.schemas.anime import Anime
        await con.run_sync(SQLModel.metadata.create_all)

SessionLocal = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)
async def get_session():
    async with SessionLocal() as session:
        yield session

