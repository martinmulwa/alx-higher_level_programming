#!/usr/bin/python3

"""
Script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import sys
import MySQLdb


def list_matching_states(
    user: str, password: str, database: str, user_input: str
) -> None:
    """
    Lists all states from the hbtn_0e_0_usa database
    that match the user input.

    Args:
        user (str): The username for the MySQL database.
        password (str): The password for the MySQL database.
        database (str): The name of the MySQL database.
        user_input (str): The user input to match.
    """
    connection = MySQLdb.connect(
        host="localhost", port=3306, user=user, passwd=password, db=database
    )

    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name=%s ORDER BY id ASC",
        (user_input,)
    )

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    user_input = sys.argv[4]
    list_matching_states(user, password, database, user_input)
