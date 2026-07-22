"""
Все перечисления проекта.

Использование Enum позволяет избежать хранения строк
вроде "пилот", "Пилот", "Pilot" и т.п.
"""

from enum import Enum


class PilotStatus(str, Enum):
    """Статус пилота."""

    PILOT = "pilot"
    CADET = "cadet"


class RegistrationStatus(str, Enum):
    """Статус заявки на регистрацию."""

    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


class PaymentType(str, Enum):
    """Тип оплаты полёта."""

    SUBSCRIPTION = "subscription"
    CASH = "cash"
    TRANSFER = "transfer"
    TRAINING = "training"
    TANDEM = "tandem"
    RENT = "rent"


class PaymentStatus(str, Enum):
    """Подтверждение оплаты."""

    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"


class QueueStatus(str, Enum):
    """Статус в очереди."""

    WAITING = "waiting"
    LAUNCHING = "launching"
    SUCCESS = "success"
    CANCELLED = "cancelled"


class UserRole(str, Enum):
    """Роль пользователя системы."""

    ADMIN = "admin"
    OPERATOR = "operator"
    DISPATCHER = "dispatcher"