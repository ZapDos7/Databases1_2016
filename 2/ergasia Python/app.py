import pymysql
import settings
from bottle import run, route, template

@route('/')
def connection():
    conn=pymysql.connect(
        settings.mysql_host,
        settings.mysql_user,
        settings.mysql_passwd,
        settings.mysql_schema,
        charset="utf8")

    cur=conn.cursor()

    cur.execute("SELECT * FROM kalitexnis")

    test_tuple=cur.fetchall()

    cur.close()
    conn.close()

    return template('temp.tpl',result = test_tuple)

run(host='localhost',port=9090)

