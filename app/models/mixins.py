"""
Mixins содержат набор полей,
которые используются сразу в нескольких моделях.

Например, RegistrationRequest и Pilot
имеют практически одинаковые персональные данные.
"""

from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .enums import PilotStatus


class PersonMixin:
    """
    Общие поля человека.

    Используется в:
    - RegistrationRequest
    - Pilot
    """

    last_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        comment="Фамилия"
    )

    first_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        comment="Имя"
    )

    middle_name: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
        comment="Отчество"
    )

    phone: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        comment="Телефон"
    )

    emergency_contact_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        comment="Доверенное лицо"
    )

    emergency_contact_phone: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        comment="Телефон доверенного лица"
    )

    pilot_number: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        comment="Уникальный четырёхзначный номер пилота"
    )

    status: Mapped[PilotStatus] = mapped_column(
        nullable=False,
        comment="Статус пилота"
    )