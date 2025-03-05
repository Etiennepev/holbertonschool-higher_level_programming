#!/usr/bin/python3
"""
lists all cities
"""

import MySQLdb
import sys

if __name__ == "__main__":

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         user=mysql_username,
                         password=mysql_password,
                         db=database_name,
                         port=3306)

    cursor = db.cursor()
    cursor.execute("""
                SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                ORDER BY cities.id ASC;""")

    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()
