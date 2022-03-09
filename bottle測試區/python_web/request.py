from bottle import  Bottle,template
from bottle import request,response
bt = Bottle()
@bt.route('/hello')
def hello():
 
    response.add_header('sss','aaa')
    return template('index.html')
 
bt.run(host='localhost', port=8080, debug=True)