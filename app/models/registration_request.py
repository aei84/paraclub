from app.models.enums import RegistrationStatus

from .mixins import PersonMixin # прачильно что добавил сюда?
from .base import BaseModel # прачильно что добавил сюда?
from sqlalchemy.orm import Mapped #???
from sqlalchemy.orm import mapped_column #???

class RegistrationRequest(PersonMixin, BaseModel):
    __tablename__ = "registration_requests"

    registration_status: Mapped[RegistrationStatus] = mapped_column(
        nullable=False,
        default=RegistrationStatus.PENDING,
        comment="Статус заявки"
)