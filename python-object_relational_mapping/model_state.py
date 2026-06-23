#!/usr/bin/python3
"""This module defines the State class and Base."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """This class represents the states table."""

    __tablename__ = "states"

    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False)

    name = Column(String(128), nullable=False)
