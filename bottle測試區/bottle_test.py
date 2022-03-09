from bottle import Bottle, run, template
app = Bottle()




@app.route('/hello')
def hello():
    return "Hello World!"



@app.route('/hello/<name>')
def greet(name):
    return template('Hello {{name}}, how are you?',name = name)

run(app, host='localhost', port=8080)