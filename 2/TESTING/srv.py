import PyMySQL

conn = MySQLdb.connect(host = "localhost", user = "usr", passwd = "testpass", db = "db")
cursor = conn.cursor
cursor.execute("SELECT VERSION()")
row = cursor.fetchone()
print"server version:", row[0]
cursor.close()
conn.close()

@app.route('/show/:<tem>')
def show(item, db):
    db.execute('SELECT * from items where name="%s"', (item,))
    row = db.fetchone()
    if row:
        return template('showitem', page=row)
    return HTTPError(404, "Page not found")

import bottle
from bottle import route, run, template, static_file

import mysql.connector

cnx = mysql.connector.connect(user='user', password='pass',
                              host='localhost',
                              database='db')
cnx.close()

@route('/static/<filename:path>')
def send_static():
    return static_file(filename, root='./')

@route('/')
def index():
    return template('index.tpl')

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


@route('/test')
def index():
    output = '<b>It has to work! This is obviously not very complex</b>'
    return output

run(host='localhost', port=8080, debug=True, reloader = True)
