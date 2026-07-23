"""
Бизнес-логика регистрации.
"""

from app.models.registration_request import RegistrationRequest
from app.repositories.registration_repository import RegistrationRepository


class RegistrationService:

    def __init__(
        self,
        registration_repository: RegistrationRepository,
        pilot_repository,
    ):

        self.registration_repository = registration_repository
        self.pilot_repository = pilot_repository

    # --------------------------------------------------------

    def register(self, data):

        #
        # Проверяем номер телефона
        #

        if self.registration_repository.get_by_phone(data.phone):

            raise ValueError(
                "Телефон уже зарегистрирован."
            )

        #
        # Проверяем четырёхзначный номер
        #

        if self.registration_repository.exists_number(
                data.pilot_number):

            raise ValueError(
                "Четырёхзначный номер уже используется."
            )

        if self.pilot_repository.exists_number(
                data.pilot_number):

            raise ValueError(
                "Четырёхзначный номер уже используется."
            )

        #
        # Создаём заявку
        #

        registration = RegistrationRequest(**data.model_dump())

        return self.registration_repository.create(
            registration
        )