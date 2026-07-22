class Pilot(PersonMixin, BaseModel):
    __tablename__ = "pilots"

    telegram_id: Mapped[int | None]


# from sqlalchemy.orm import Mapped, mapped_column

# from app.database.database import Base


# class Pilot(Base):
#     __tablename__ = "pilots"

#     id: Mapped[int] = mapped_column(primary_key=True)

#     first_name: Mapped[str]
#     last_name: Mapped[str]