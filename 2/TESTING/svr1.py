import MySQLdb as sql
import bottle_mysql
from bottle import route, run, template

db = sql.connect(host = 'localhost', user = 'root', passwd = 'root', db = 'db')
c = db.cursor()
c.execute('SELECT * From client')
r = c.fetchall()

@route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

@route('/test')
def index():
    for i in r:
    	return str(i[0])

run(host='localhost', port=8080, debug=True, reloader = 'True')



