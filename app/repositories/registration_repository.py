"""
Работа с таблицей registration_requests.
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.registration_request import RegistrationRequest


class RegistrationRepository:

    def __init__(self, db: Session):
        self.db = db

    # --------------------------------------------------------

    def create(self, registration: RegistrationRequest):

        self.db.add(registration)
        self.db.commit()
        self.db.refresh(registration)

        return registration

    # --------------------------------------------------------

    def get_by_phone(self, phone: str):

        stmt = (
            select(RegistrationRequest)
            .where(RegistrationRequest.phone == phone)
        )

        return self.db.scalar(stmt)

    # --------------------------------------------------------

    def exists_number(self, number: int):

        stmt = (
            select(RegistrationRequest)
            .where(RegistrationRequest.pilot_number == number)
        )

        return self.db.scalar(stmt) is not None