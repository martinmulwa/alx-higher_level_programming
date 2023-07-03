#!/usr/bin/python3
""" Script that takes in the name of a state as an argument and lists
    all cities of that state, using the database hbtn_0e_4_usa.
"""

if __name__ == '__main__':
    # Import necessary modules
    import sys
    import MySQLdb as sql

    # Extract command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    user_input = sys.argv[4]

    # Split user input to prevent SQL injection
    state_name = user_input.split("'")[0]

    # Connect to the MySQL database
    connection = sql.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    )

    # Create a cursor object to execute queries
    cursor = connection.cursor()

    # Execute the query to retrieve all cities of the given state
    cursor.execute("SELECT c.name\
        FROM states s\
        JOIN cities c\
        ON s.id = c.state_id\
        WHERE s.name = '{}' ORDER BY c.id".format(state_name))

    # Retrieve all rows returned by the query
    rows = cursor.fetchall()

    # Print the matching rows to the console
    print(", ".join([row[0] for row in rows]))

    # Close the cursor and the connection to the MySQL database
    cursor.close()
    connection.close()
