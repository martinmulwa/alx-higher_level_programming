#!/usr/bin/python3

"""
Script that prints all City objects from the hbtn_0e_14_usa database
"""

# Standard Library imports
import sys

# Third-party imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Local application imports
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    # Create a database engine using the provided credentials
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session factory using the database engine
    Session = sessionmaker(bind=engine)

    # Create a session instance
    session = Session()

    # Query the database for all City objects, ordered by ID,
    # with their associated State objects
    all_cities = session.query(State, City).join(City).order_by(City.id).all()

    # Print each City object's name, ID, and associated State object's name
    for state, city in all_cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
