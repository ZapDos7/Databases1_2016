from bottle import route, run, template

@route('/')
@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}!',name=name)

run(host='localhost', port=8090, debug=True)