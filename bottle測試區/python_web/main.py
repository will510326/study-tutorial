import  bottle
from bottle import request, run,template
from beaker.middleware import SessionMiddleware
app = bottle.default_app()
@app.get('/')
def hello():
    s = request.environ.get('beaker.session')
    print(s)
    s['user'] = "wt"
    s.save()
    return "hello"
@app.route('/hello/<name>')
def hello(name):
    s = request.environ.get('beaker.session')
    print(s)
    return template('index.html', name = name)
session_opts = {
        'session.type': 'file',
        'session.cookie_expires': 100,
        'session.data_dir': './session',
        'session.auto': True
        }
app = SessionMiddleware(app, session_opts)
run(app = app, host='localhost', port='8080', reloader = True)