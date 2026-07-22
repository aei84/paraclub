"""
Базовые классы моделей.

Все таблицы проекта наследуются от BaseModel.
Здесь находятся общие поля, которые есть практически у каждой таблицы.
"""

from datetime import datetime

from sqlalchemy import DateTime, func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    """Базовый класс SQLAlchemy."""
    pass


class BaseModel(Base):
    """
    Общая модель для всех таблиц.

    Содержит:
    - первичный ключ
    - дату создания записи
    - дату последнего изменения
    """

    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
        comment="Дата создания записи"
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
        comment="Дата последнего изменения"
    )