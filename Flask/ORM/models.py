from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False
    )

    addresses: Mapped[list["Address"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )

    cars: Mapped[list["Car"]] = relationship(
        back_populates="user"
    )

    def __repr__(self):
        return (
            f"User("
            f"id={self.id}, "
            f"name='{self.name}', "
            f"email='{self.email}'"
            f")"
        )


class Address(Base):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    street: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    city: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    state: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    user: Mapped["User"] = relationship(
        back_populates="addresses"
    )

    def __repr__(self):
        return (
            f"Address("
            f"id={self.id}, "
            f"street='{self.street}', "
            f"city='{self.city}', "
            f"state='{self.state}', "
            f"user_id={self.user_id}"
            f")"
        )


class Car(Base):
    __tablename__ = "cars"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    brand: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    model: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    year: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True
    )

    user: Mapped["User | None"] = relationship(
        back_populates="cars"
    )

    def __repr__(self):
        return (
            f"Car("
            f"id={self.id}, "
            f"brand='{self.brand}', "
            f"model='{self.model}', "
            f"year={self.year}, "
            f"user_id={self.user_id}"
            f")"
        )