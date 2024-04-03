from sqlalchemy.orm import Mapped, mapped_column

from db import Base


class Country(Base):
    __tablename__ = 'country'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    population: Mapped[int]
    region: Mapped[str]
