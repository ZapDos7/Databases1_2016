import pymysql
import settings
from bottle import run, route, template

@route('/')
def test():
    conn=pymysql.connect(
        settings.mysql_host,
        settings.mysql_user,
        settings.mysql_passwd,
        settings.mysql_schema,
        charset="utf8")

    cur=conn.cursor()

    cur.execute("SELECT epitheto FROM kalitexnis")

    test_tuple=cur.fetchall()

    for row in test_tuple:
        u=row[0].encode('utf8')
        print(u)

    cur.close()
    conn.close()

    info={'test_tuple': test_tuple}

    return template('temp.tpl',info)

run(host='localhost',port=9090, debug = True, reloader = True)
