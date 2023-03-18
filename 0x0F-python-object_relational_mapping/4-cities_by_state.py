#!/usr/bin/python3
"""Mysql module that allows you to select costom state
 Usage: ./2-filter_class: <user>
                            <password>
                            <database>
                            <filter>
"""

import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM cities
                   JOIN states ON cities.id = states.id ORDER BY cities.id ASC;""")
    rows = cursor.fetchall()
    [print(row) for row in rows]
