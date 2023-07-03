#!/usr/bin/python3
""" Module that contains the class definition of a State and an instance.
"""

# Import necessary modules
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for declarative class definitions
Base = declarative_base()

# Define the State class


class State(Base):
    """ Class representing a state in the hbtn_0e_6_usa database.

    Inherits from the Base class provided by SQLAlchemy. Links to the MySQL
    table states, with class attributes representing the columns of the table.
    """
    __tablename__ = 'states'

    # Define class attributes representing the columns of the table
    id = Column(Integer(), primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
