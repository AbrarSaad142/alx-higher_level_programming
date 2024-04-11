#!/usr/bin/python3
""" takes in an argument and displays all values in the states
 table of hbtn_0e_0_usa where name matches the argument.
"""
from sys import argv
import MySQLdb

MY_HOST = 'localhost'

if __name__ == "__main__":
    db = MySQLdb.Connect(host=MY_HOST, port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE BINARY name = %s
                 """, [argv[4]])
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    db.close()
