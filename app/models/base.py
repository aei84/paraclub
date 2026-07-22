"""
Базовые классы моделей проекта.

Каждая таблица наследуется от BaseModel.

Base отвечает за работу SQLAlchemy.

BaseModel добавляет поля,
которые есть практически во всех таблицах:
    - id
    - created_at
    - updated_at
"""

from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped #???
from sqlalchemy.orm import mapped_column #???


class Base(DeclarativeBase):
    """
    Базовый класс SQLAlchemy.

    Все ORM-модели проекта наследуются
    (через BaseModel) именно от него.
    """

    pass


class BaseModel(Base):
    """
    Общая модель для всех таблиц проекта.

    Содержит:
        id
        created_at
        updated_at
    """

    __abstract__ = True

    id: Mapped[int] = mapped_column(
        primary_key=True,
        comment="Первичный ключ"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),#???
        nullable=False, #???
        comment="Дата создания записи"
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
        comment="Дата последнего изменения"
    )