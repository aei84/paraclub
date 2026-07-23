"""
Pydantic-схемы регистрации пилотов.
"""

from pydantic import BaseModel, Field


class RegistrationCreate(BaseModel):
    """
    Данные, которые вводит пилот при регистрации.
    """

    last_name: str = Field(..., max_length=100)
    first_name: str = Field(..., max_length=100)
    middle_name: str | None = Field(default=None, max_length=100)

    phone: str = Field(..., max_length=20)

    emergency_contact_name: str = Field(..., max_length=150)
    emergency_contact_phone: str = Field(..., max_length=20)

    pilot_number: int = Field(..., ge=1000, le=9999)

    status: str


class RegistrationResponse(BaseModel):
    """
    Ответ после успешной регистрации.
    """

    id: int
    message: str