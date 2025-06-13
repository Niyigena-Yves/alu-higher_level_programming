#!/usr/bin/python3
"""
The script to list all cities from the db
takes 3 arguments
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
    JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
    lst = cur.fetchall()
    for r in lst:
        print(r)
    cur.close()
    db.close()
