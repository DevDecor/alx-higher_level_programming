#!/usr/bin/python3
"""Mysql module that fetches all states from states database
 Usage: ./1-lter_states.py
                    <user>
                    <password>
                    <database>
    Fetches all states
    from the database
"""

import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE name REGEXP '^N'
                   ORDER BY id ASC;""")
    rows = cursor.fetchall()
    [print(row) for row in rows if row[1][0] == 'N']
