from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from src.properties import DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=True)
session = async_sessionmaker(engine, expire_on_commit=False)


async def get_session():
    async with session() as new_session:
        yield new_session


SessionDepend = Annotated[AsyncSession, Depends(get_session)]
