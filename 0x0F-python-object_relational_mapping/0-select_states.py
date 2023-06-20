#!/usr/bin/python3
# Lists all states from hbtn_0e_0_usa database
# Usage: ./0-select_states.py <mysql.username> \
#                             <mysql.password> \
#                             <database name>

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host=127.0.0.1, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`")
    res = cur.fetchall()

    for state in res:
        print(state)
