#!/usr/bin/python3

"""
Script that creates the State "California" with the City "San Francisco"
in the hbtn_0e_100_usa database
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

    # Create State and City tables in the database if they don't already exist
    Base.metadata.create_all(engine)

    # Create a session factory using the database engine
    Session = sessionmaker(bind=engine)

    # Create a session instance
    session = Session()

    # Create a new City object with a new State object
    city1 = City(name='San Francisco', state=State(name='California'))

    # Add City object to the session and commit the changes to the database
    session.add(city1)
    session.commit()
