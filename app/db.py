from pydantic import PostgresDsn
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession

from .config import DatabaseSettings

database_settings = DatabaseSettings()


def assemble_database_url(settings: DatabaseSettings, as_async: bool = True):
    assert settings.host is not None
    assert settings.port is not None

    port = str(settings.port)

    scheme = "postgresql+asyncpg" if as_async else "postgresql"

    return PostgresDsn.build(
        scheme=scheme,
        user=settings.user,
        password=settings.password,
        host=settings.host,
        port=port,
        path=f"/{settings.name}",
    )


engine = AsyncEngine(create_engine(assemble_database_url(database_settings), echo=True, future=True))


async def init_db():
    async with engine.begin() as conn:
        # await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session():
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session
