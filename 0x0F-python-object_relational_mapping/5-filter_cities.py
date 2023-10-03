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
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON states.id=cities.state_id "
        "WHERE states.name=%s"
    )
    cursor.execute(query, (sys.argv[4],))
    cities = cursor.fetchall()

    for city in range(0, len(cities)):
        if city+1 != len(cities):
            print(cities[city][0], end=", ")
        else:
            print(cities[city][0], end="")
    print()
    cursor.close()
    db.close()
