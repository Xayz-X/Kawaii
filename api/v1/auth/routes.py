
from fastapi import APIRouter, Depends
from .model import AuthCredential
from api.crud.db import get_session
from sqlalchemy.ext.asyncio.session import AsyncSession


auth_route = APIRouter()



@auth_route.post("/token")
async def auth_login(credential: AuthCredential, session: AsyncSession = Depends(get_session)):
    ...


    