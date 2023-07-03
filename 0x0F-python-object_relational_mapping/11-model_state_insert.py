#!/usr/bin/python3

"""
Adds the State object "Louisiana" to the hbtn_0e_6_usa database
"""

# Standard Library imports
import sys

# Third-party imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Local application imports
from model_state import Base, State

if __name__ == '__main__':
    # Create a database engine using the provided credentials
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session factory using the database engine
    Session = sessionmaker(bind=engine)

    # Create a session instance
    session = Session()

    # Create a new State object and add it to the session
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the ID of the new State object
    print(new_state.id)
