"""
Database model for the books class
"""

import datetime
from sqlmodel import Column, SQLModel, Field, true
from uuid import UUID
import sqlalchemy.dialects.postgresql as pg


class book(SQLModel, table=true):
    __tablename__ = "books"
    uid: UUID = Field(
        sa_column=Column(
            pg.UUID,
            primary_key=true,
            unique=true,
            nullable=true,
        )
    )
    title: str
    price: int
    publisher: str
    createdAt: Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
