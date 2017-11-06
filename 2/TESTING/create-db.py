import bottle
from bottle import route, run, template

import bottle_mysql
plugin = bottle_mysql.Plugin(dbuser='user', dbpass='pass', dbname='db')

#import pymysql
#import sys

con = pymysql.connect('todo.dat')

print "Creating database/table..."

with con:
	cur = con.cursor()
	# DROP TABLE
	#cur.execute("DROP TABLE IF EXISTS test")

	# CREATE TABLES
	cur.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, desc TEXT, datetime TEXT )")

con.close()
print "Database/table created."
