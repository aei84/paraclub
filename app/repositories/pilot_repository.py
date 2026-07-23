"""
Репозиторий для работы с таблицей pilots.
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.pilot import Pilot


class PilotRepository:
    """
    Работа с таблицей pilots.

    Репозиторий не содержит бизнес-логики.
    Он только читает и изменяет данные в БД.
    """

    def __init__(self, db: Session):
        self.db = db

    # ---------------------------------------------------------
    # Создание
    # ---------------------------------------------------------

    def create(self, pilot: Pilot) -> Pilot:
        """
        Создать нового пилота.
        """

        self.db.add(pilot)
        self.db.commit()
        self.db.refresh(pilot)

        return pilot

    # ---------------------------------------------------------
    # Получение
    # ---------------------------------------------------------

    def get_by_id(self, pilot_id: int) -> Pilot | None:
        """
        Получить пилота по ID.
        """

        stmt = (
            select(Pilot)
            .where(Pilot.id == pilot_id)
        )

        return self.db.scalar(stmt)

    def get_by_phone(self, phone: str) -> Pilot | None:
        """
        Получить пилота по телефону.
        """

        stmt = (
            select(Pilot)
            .where(Pilot.phone == phone)
        )

        return self.db.scalar(stmt)

    def get_by_number(self, pilot_number: int) -> Pilot | None:
        """
        Получить пилота по четырехзначному номеру.
        """

        stmt = (
            select(Pilot)
            .where(Pilot.pilot_number == pilot_number)
        )

        return self.db.scalar(stmt)

    def get_by_telegram(self, telegram_id: int) -> Pilot | None:
        """
        Получить пилота по Telegram ID.
        """

        stmt = (
            select(Pilot)
            .where(Pilot.telegram_id == telegram_id)
        )

        return self.db.scalar(stmt)

    def get_all(self) -> list[Pilot]:
        """
        Получить список всех пилотов.
        """

        stmt = (
            select(Pilot)
            .order_by(
                Pilot.last_name,
                Pilot.first_name,
            )
        )

        return list(self.db.scalars(stmt))

    # ---------------------------------------------------------
    # Проверки существования
    # ---------------------------------------------------------

    def exists_id(self, pilot_id: int) -> bool:
        return self.get_by_id(pilot_id) is not None

    def exists_phone(self, phone: str) -> bool:
        return self.get_by_phone(phone) is not None

    def exists_number(self, pilot_number: int) -> bool:
        return self.get_by_number(pilot_number) is not None

    def exists_telegram(self, telegram_id: int) -> bool:
        return self.get_by_telegram(telegram_id) is not None

    # ---------------------------------------------------------
    # Обновление
    # ---------------------------------------------------------

    def update(self) -> None:
        """
        Сохранить изменения объекта Pilot.

        Предполагается, что объект уже был изменен.
        """

        self.db.commit()

    # ---------------------------------------------------------
    # Удаление
    # ---------------------------------------------------------

    def delete(self, pilot: Pilot) -> None:
        """
        Удалить пилота.
        """

        self.db.delete(pilot)
        self.db.commit()