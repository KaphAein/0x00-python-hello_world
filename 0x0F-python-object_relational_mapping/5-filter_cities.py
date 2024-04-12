#!/usr/bin/python3
'''lists all cities from the database hbtn_0e_0_usa'''
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    query = ('SELECT cities.id, cities.name FROM cities '
             'INNER JOIN states ON cities.state_id = states.id '
             'WHERE states.name = %s ORDER BY cities.id ASC')
    cur.execute(query, (argv[4], ))
    rows = cur.fetchall()
    cities = []
    for row in rows:
        cities.append(row[1])
    print(", ".join(cities))

    cur.close()
    db.close()
