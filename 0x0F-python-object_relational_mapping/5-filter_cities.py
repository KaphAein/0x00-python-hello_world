#!/usr/bin/python3
'''lists all cities from the database hbtn_0e_0_usa'''
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    query = 'SELECT cities.id, cities.name FROM cities '
    'INNER JOIN states ON cities.state_id = states.id '
    'WHERE states.name = %s ORDER BY cities.id ASC'
    cur.execute(query, (argv[4], ))
    print(", ".join(map(lambda x: x[0], cur.fetchall())))
    cur.close()
    db.close()
