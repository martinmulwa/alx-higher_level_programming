#!/usr/bin/python3
""" Script that lists all cities from the database hbtn_0e_4_usa.
"""

if __name__ == '__main__':
    # Import necessary modules
    import sys
    import MySQLdb as sql

    # Extract command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

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

    # Execute the query to retrieve cities with their corresponding state names
    cursor.execute("""SELECT c.id, c.name, s.name
                FROM cities c
                JOIN states s
                ON c.state_id=s.id
                ORDER BY c.id ASC""")

    # Retrieve all rows returned by the query
    rows = cursor.fetchall()

    # Print the matching rows to the console
    for row in rows:
        print("{}".format(row))

    # Close the cursor and the connection to the MySQL database
    cursor.close()
    connection.close()
