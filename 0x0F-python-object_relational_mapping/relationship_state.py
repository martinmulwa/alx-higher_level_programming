#!/usr/bin/python3

"""
Module containing the definition of the State class
and its associated table in the database
"""

# Third-party imports
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Declare a base class for declarative models
Base = declarative_base()


class State(Base):
    """State class
    """
    __tablename__ = 'states'

    id = Column(Integer(), primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref='state')
