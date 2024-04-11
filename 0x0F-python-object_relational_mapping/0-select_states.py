#!/usr/bin/python3
from sys import argv
import MySQLdb

MY_HOST = 'localhost'

if __name__ == "__main__":
    db = MySQLdb.Connect(host=MY_HOST, port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    db.close()
