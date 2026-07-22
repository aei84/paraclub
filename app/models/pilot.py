# я думал что все импорты возьмуться из __init__.py
import app.models
from .mixins import PersonMixin # прачильно что добавил сюда?
from .base import BaseModel # прачильно что добавил сюда?
from sqlalchemy.orm import Mapped #???
from sqlalchemy.orm import mapped_column #???

class Pilot(PersonMixin, BaseModel):
    __tablename__ = "pilots"

    telegram_id: Mapped[int | None] = mapped_column(
        nullable=True,
        unique=True,
        comment="Telegram ID пользователя"
)
