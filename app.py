from flask import Flask
from flask import render_template
from flask import request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    name = 'James'
    return render_template('index.html', title='Welcome', username=name)

@app.route('/hello')
def hello_world():
    return "hello world"

@app.route('/dashboard/<name>')
def dashboard(name):
    return f"welcome {name}"

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('dashboard', name=user))
    else:
        user = request.args.get('name')
        return render_template('login.html')

app.run(host='0.0.0.0', port=81)