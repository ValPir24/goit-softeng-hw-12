from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+asyncpg://postgres:your_password@db:5432/your_database"

# Створення асинхронного engine
engine = create_async_engine(DATABASE_URL, echo=True, pool_size=10, max_overflow=20)

# Створення SessionLocal для роботи з базою даних
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

Base = declarative_base()

async def async_create_all():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

async def close_db_session():
    await SessionLocal.close()

async def cleanup_db_session():
    await engine.dispose()
