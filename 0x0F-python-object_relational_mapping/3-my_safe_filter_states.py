#!/usr/bin/python3
""" Script that takes in arguments and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument.
    This version is safe from MySQL injections.
"""

if __name__ == '__main__':
    # Import necessary modules
    import sys
    import MySQLdb as sql

    # Extract command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    name_to_find = sys.argv[4]

    # Split user input to prevent SQL injection
    name_to_find = name_to_find.split("'")[0]

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

    # Execute the query to retrieve all rows from the states table
    # where the name matches the given input
    cursor.execute("SELECT * FROM states WHERE name='{}'\
                ORDER BY id".format(name_to_find))

    # Retrieve all rows returned by the query
    rows = cursor.fetchall()

    # Print the matching rows to the console
    for row in rows:
        print(row)

    # Close the cursor and the connection to the MySQL database
    cursor.close()
    connection.close()
