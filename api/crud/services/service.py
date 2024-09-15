from sqlmodel.ext.asyncio.session import AsyncSession
from api.schemas.anime import Anime
from sqlalchemy.future import select
from sqlalchemy import func

class AnimeService:
    async def get_specific_anime_by_id(self, anime_id: int, session: AsyncSession):
        """Get a single anime data by the id."""
        # just count the rows aavailbe on thsi table and print
        query = select(Anime).where(Anime.id == anime_id) # it ill retuen all columsn right?
        result = await session.exec(query)
        first_result = result.scalars().first()
        return first_result


    async def count_anime_rows(self, session: AsyncSession) -> int:
        """Count the total number of rows in the Anime table."""
        query = select(func.count()).select_from(Anime)
        result = await session.exec(query)
        count = result.scalar()  # Get the count result
        print(f"Total rows in Anime table: {count}")
        return count