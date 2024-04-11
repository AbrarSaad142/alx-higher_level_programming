#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa"""
from sys import argv
import MySQLdb

MY_HOST = 'localhost'

if __name__ == "__main__":
    db = MySQLdb.Connect(host=MY_HOST, port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities
                INNER JOIN states ON cities.state_id = states.id
                ORDER BY id ASC""")
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    db.close()
