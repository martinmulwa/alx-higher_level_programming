#!/usr/bin/python3

"""
Module containing the definition of the City class and
its associated table in the database
"""

# Third-party imports
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey

# Local application imports
from model_state import Base


class City(Base):
    """City class"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
