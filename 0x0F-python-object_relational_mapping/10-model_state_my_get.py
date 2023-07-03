#!/usr/bin/python3
""" Script that lists all State objects that contain the letter 'a'
    from the database hbtn_0e_6_usa.
"""

if __name__ == '__main__':
    # Import necessary modules
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    # Import the Base and State classes from the model_state module
    from model_state import Base, State

    # Connect to the MySQL database using the given command line arguments
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    # Create a session object using the connection
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve all State objects that contain the letter 'a' from the database
    states_with_a = session.query(State)\
        .filter(State.name.like('%a%'))\
        .order_by(State.id)

    # Print the matching State objects to the console
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))
