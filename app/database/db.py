from pydantic import PostgresDsn
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.pool import NullPool
from sqlmodel.ext.asyncio.session import AsyncSession

from ..config.database_settings import DatabaseSettings

database_settings = DatabaseSettings()


def assemble_database_url(settings: DatabaseSettings, as_async: bool = True):
    assert settings.host is not None
    assert settings.port is not None

    port = int(settings.port)

    scheme = "postgresql+asyncpg" if as_async else "postgresql"
    # pylint: disable=no-member
    return PostgresDsn.build(
        scheme=scheme,
        username=settings.user,
        password=settings.password,
        host=settings.host,
        port=port,
        path=f"{settings.name}",
    )


engine = create_async_engine(
    assemble_database_url(database_settings).unicode_string(), echo=True, future=True, poolclass=NullPool
)


async def get_session():
    async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session
