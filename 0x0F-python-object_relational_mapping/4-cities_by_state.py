#!/usr/bin/python3
"""
A script that selects all data from user cities table
In ascending order.
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.Connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    cursor = db.cursor()
    query = (
        "SELECT cities.id, "
        "cities.name, "
        "states.name "
        "FROM cities "
        "JOIN states ON states.id=cities.state_id"
    )
    cursor.execute(query)
    cities = cursor.fetchall()

    for city in cities:
        print(city)
    cursor.close()
    db.close()
