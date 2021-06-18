<<<<<<< HEAD
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/second')
def second():
    return 'Bize Her Yer Dünya'

@qpp.route('/third/subthird')
def third():
    return 'This is the subpage of third page'

@app.route('/fourth/<string:id>')
def fourth(id):
    return f'Id number of this page is {id}'


if __name__=='__main__':
    app.run(debug=True)
=======
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/second')
def second():
    return 'Bize Her Yer Dünya'

@qpp.route('/third/subthird')
def third():
    return 'This is the subpage of third page'

@app.route('/fourth/<string:id>')
def fourth(id):
    return f'Id number of this page is {id}'


if __name__=='__main__':
    app.run(debug=True)
>>>>>>> ab51eb81fecc0541741c7ec88e8b61e8267b9306
