from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

db = SQLAlchemy()


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    favorites: Mapped["FavoritesList"] = relationship(back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Character(db.Model):  # molde para rellenar
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    specie: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)

    def serialize(self):   # te da los datos con los que se rellenó
        return {
            "id": self.id,
            "name": self.name,
            "specie": self.specie,
        }


class FavoritesList(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user: Mapped["User"] = relationship(back_populates="favorites")
    # relacion de 1 lista de favoritos con muchos personajes
    favorite_characters: Mapped[List["Character"]
                                ] = relationship(back_populates="favorite")

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user,
        }
