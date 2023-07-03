#!/usr/bin/python3

"""
Prints the State object with the specified name from the hbtn_0e_6_usa database
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

    # Get the user input and extract the name of the state
    user_input = sys.argv[4].split("'")
    state_name = user_input[0]

    # Query the database for the state with the specified name
    state = session.query(State).filter(State.name == state_name).first()

    # If the state is found, print its ID
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
