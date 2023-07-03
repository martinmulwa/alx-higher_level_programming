#!/usr/bin/python3

"""
Script that connects to a MySQL server running on localhost at port 3306
and retrieves rows from the cities table where the state name matches
"California". The results are sorted in ascending order by the cities.id column
"""

import sys
import MySQLdb


def get_cities_by_state(username, password, database, state_name):
    """
    Connects to a MySQL server running on localhost at port 3306
    and retrieves rows from the cities table where the state name matches
    the specified state_name. The results are sorted in ascending order by
    the cities.id column.
    """
    # Connect to MySQL server
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create cursor
    cursor = connection.cursor()

    # Execute SQL query
    query = "SELECT cities.id, cities.name, states.name FROM cities \
             JOIN states ON cities.state_id = states.id \
             WHERE states.name LIKE %s ORDER BY cities.id ASC"
    cursor.execute(query, (state_name,))

    # Print results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    connection.close()


if __name__ == '__main__':
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = 'California'

    # Call function to retrieve cities by state
    get_cities_by_state(username, password, database, state_name)
