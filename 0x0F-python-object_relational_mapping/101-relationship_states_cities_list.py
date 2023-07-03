#!/usr/bin/python3

"""
Script that lists all State objects and their corresponding City objects
in the hbtn_0e_101_usa database
"""

# Standard Library imports
import sys

# Third-party imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Local application imports
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    # Create a database engine using the provided credentials
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session factory using the database engine
    Session = sessionmaker(bind=engine)

    # Create a session instance
    session = Session()

    # Query the database for all State objects, ordered by ID
    states = session.query(State).order_by(State.id).all()

    # Loop through each State object and print its name
    # and its associated City objects' names
    for count, state in enumerate(states):
        print("{}: {}".format(count + 1, state.name))
        for index, city in enumerate(state.cities):
            print("    {}: {}".format(index + 1, city.name))
