#!/usr/bin/python3

"""
Module that lists all states with a name starting with 'N' (uppercase)
from the hbtn_0e_0_usa database.
"""

import sys
import MySQLdb


def list_states(user: str, password: str, database: str) -> None:
    """
    Lists all states with a name starting with 'N' (uppercase)
    from the hbtn_0e_0_usa database.
    """
    connection = MySQLdb.connect(
        host="localhost", port=3306, user=user, passwd=password, db=database
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")

    rows = cursor.fetchall()

    for row in rows:
        if row[1].startswith("N"):
            print(row)

    cursor.close()
    connection.close()


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    list_states(user, password, database)
