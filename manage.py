from flask import Flask, render_template, url_for
from flask_script import Manager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html', name = 'Joe.C.Zhou'), 200

@app.route('/index')
def user():
    return 'Hello Flask'

@app.errorhandler(404)
def not_found():
    return render_template('404.html'), 404

@app.errorhandler(403)
def not_found():
    return render_template('403.html'), 403

@app.errorhandler(500)
def not_found():
    return render_template('500.html'), 500

if __name__ == '__main__':
    manager.run()