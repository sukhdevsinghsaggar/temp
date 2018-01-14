import random
from flask import Flask, render_template

app = Flask(__name__, static_folder='../static/dist', template_folder='../static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/host')
def host():
    return render_template('host.html')
  
@app.route('/signup')
def signup():
    return render_template('signup.html')
  
@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
