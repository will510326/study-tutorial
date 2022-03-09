import  bottle
from bottle import request, run
from beaker.middleware import SessionMiddleware
 
app = bottle.default_app()
 
@app.error(500)
@app.error(400)  # Bad Request
@app.error(401)  # Unauthorized
@app.error(403)  # Forbidden
@app.error(404)  # Not Found
@app.error(405)
@app.get('/')
def hello():
    s = request.environ.get('beaker.session')
    print(s)
    s['user'] = "wt"
    s.save()
    return "hello"
 
@app.get('/login')
def hello():
    s = request.environ.get('beaker.session')
    print(s)
    return "hello"
 
session_opts = {
        'session.type': 'file',
        'session.cookie_expires': 100,
        'session.data_dir': './session',
        'session.auto': True
        }

app = SessionMiddleware(app, session_opts)

run(app = app, host='localhost', port='8080',debug=True, reloader = True)
