#!/usr/bin/python3
import MySQLdb
import sys
if __name__ == '__main__':
    db_connection= MySQLdb.connect(host="localhost", port=3306, user=f"{sys.argv[1]}", passwd=f"{sys.argv[2]}", db=f"{sys.argv[3]}", charset="utf8")
    cur = db_connection.cursor()
    query = query = "SELECT * FROM states"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    db_connection.close()
