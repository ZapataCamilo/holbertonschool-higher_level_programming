#!/usr/bin/python3
"""
 takes in the name of a state as an argument and
 lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    argname = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                JOIN states ON cities.state_id = states.id\
                AND states.name = '{}'\
                ORDER BY cities.id".format(argname))
    query_rows = cur.fetchall()
    res = []
    for row in query_rows:
        res.append(row[0])

    print(", ".join(res))
    cur.close()
    conn.close()
