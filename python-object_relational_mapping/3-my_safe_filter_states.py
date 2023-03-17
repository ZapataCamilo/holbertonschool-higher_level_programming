#!/usr/bin/python3
"""
TRUNCATE TABLE
"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    matchename = sys.argv[4].split(';')[0].strip("'")

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY'{}'\
                ORDER BY states.id ASC".format(matchename))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
