'''main entrypoint for the application'''
from flask import Flask, render_template, request, session, redirect
app = Flask(__name__, '/', '/')

@app.route('/')
@app.route('/index.html')
@app.route('/index', methods=['get'])
def index():
    'Main template route'
    return render_template('index.html')
@app.route('/login', methods=['post', 'get'])
@app.route('/login.html', methods=['get'])
def auth():
    'Authentication endpoint'
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        #placeholder to validate password here
        if True:
            session['username'] = username
            return render_template('index.html')
        return render_template('login.html')
    else:
        return render_template('login.html')
@app.route('/search', methods=['post'])
def search(term, services):
    'Route to search'
    #placeholder to ping the apis
    return render_template('index.html')
@app.route('/signup', methods=['get', 'post'])
@app.route('/signup.html', methods=['get'])
def sign_up():
    'Sign up a new user'
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        #placeholder for saving the user information in the db
        return render_template('index.html')
    else:
        return render_template('signup.html')
