"""
Настройка Alembic.

Этот файл отвечает за создание и применение миграций.

Alembic использует:
    - настройки подключения из app.core.config
    - все ORM-модели из app.models
    - metadata SQLAlchemy для сравнения моделей с базой данных.
"""

from logging.config import fileConfig

from alembic import context
from sqlalchemy import create_engine, engine_from_config, pool

from app.core.config import settings

# Импортируем ВСЕ модели.
# Благодаря этому SQLAlchemy зарегистрирует их в Base.metadata.
import app.models  # noqa: F401

from app.models.base import Base


# ------------------------------------------------------------
# Конфигурация Alembic
# ------------------------------------------------------------

config = context.config

# # Передаем Alembic строку подключения из нашего config.py
# config.set_main_option(
#     "sqlalchemy.url",
#     settings.database_url.render_as_string(hide_password=False),
# )

# Настройка логирования
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


# Metadata всех моделей проекта.
target_metadata = Base.metadata


# ------------------------------------------------------------
# Offline режим
# ------------------------------------------------------------

def run_migrations_offline() -> None:
    """
    Генерация SQL без подключения к базе данных.

    Используется редко.
    """

    url = config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


# ------------------------------------------------------------
# Online режим
# ------------------------------------------------------------

def run_migrations_online() -> None:
    """
    Основной режим работы Alembic.

    Подключается к PostgreSQL,
    сравнивает модели с базой
    и выполняет миграции.
    """

    connectable = create_engine(
        settings.database_url,
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:

        context.configure(
            connection=connection,
            target_metadata=target_metadata,

            # Очень полезные параметры
            compare_type=True,
            compare_server_default=True,
        )

        with context.begin_transaction():
            context.run_migrations()


# ------------------------------------------------------------
# Запуск
# ------------------------------------------------------------

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()