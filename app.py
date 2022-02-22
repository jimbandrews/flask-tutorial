from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'James'
    return render_template('index.html', title='Welcome', username=name)

app.run(host='0.0.0.0', port=81)