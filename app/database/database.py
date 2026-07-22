"""
Работа с базой данных.

Здесь находятся:
- создание подключения к PostgreSQL;
- фабрика сессий SQLAlchemy;
- функция получения сессии для FastAPI.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.core.config import settings


# Создаем подключение к PostgreSQL
engine = create_engine(
    settings.database_url,
    echo=True,          # Показывать SQL-запросы в консоли (позже можно выключить)
    future=True, #???
)


# Фабрика сессий
SessionLocal = sessionmaker( #???
    bind=engine,
    autoflush=False,
    autocommit=False,
)


def get_db():
    """
    Генератор сессии для FastAPI.

    Использование:

    @router.get("/")
    def test(db: Session = Depends(get_db)):
        ...
    """

    db: Session = SessionLocal()

    try:
        yield db
    finally:
        db.close()