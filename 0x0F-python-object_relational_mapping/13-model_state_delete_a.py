#!/usr/bin/python3

"""
Deletes all State objects with a name containing the letter 'a' from
the hbtn_0e_6_usa database
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

    # Query the database for State objects whose names contain the letter 'a'
    states_to_delete = session.query(
        State).filter(State.name.like('%a%')).all()

    # Delete each of the State objects found and commit the changes
    for state in states_to_delete:
        session.delete(state)
    session.commit()
