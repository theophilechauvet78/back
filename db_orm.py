from sqlalchemy import (
    create_engine,
    Column,
    String,
    Integer,
    Boolean,
    DateTime,
    Date,
    Time,
    ForeignKey,
    Float,
)
from sqlalchemy.orm import *
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import Session

class Base(DeclarativeBase):
    pass


class Line(Base):
    __tablename__ = "Line"

    # Columns
    id: Mapped[int] = mapped_column(primary_key=True)
    lastname: Mapped[str] = mapped_column(String(30))
    firstname: Mapped[str] = mapped_column(String(30))

    def line_name(self, secure=False):
        if secure:
            return f"{self.firstname}_{self.lastname}"
        return (
            f"{self.firstname} / {self.lastname}"
        )

    def __repr__(self) -> str:
        return f"Line(id={self.id!r}, name={self.lastname!r}, fullname={self.firstname!r})"
