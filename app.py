'''main entrypoint for the application'''
import time
from os import environ
from src.database import Database
from src.twitterAPI import Requestor
from src.login import UserManager
from flask import Flask, render_template, request, session,redirect
app = Flask(__name__, '/static')
app.secret_key = 'rubber baby buggy bumbers'
app.config['DEBUG'] = environ.get('env') != 'PROD'
app.config['TEMPLATES_AUTO_RELOAD'] = app.config['DEBUG']

@app.route('/')
@app.route('/index.html')
@app.route('/index', methods=['get'])
def index():
    'Main template route'
    if check_for_user():
        return render_template('home.html')
    return render_template('index.html')
@app.route('/login', methods=['post', 'get'])
@app.route('/login.html', methods=['get'])
def auth():
    'Authentication endpoint'
    if request.method == 'POST':
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        user_manager = UserManager()
        if user_manager.validate_credentials(username, password):
            session['username'] = username
            session['expiration'] = time.time() + (30 * 60)
            return render_template('home.html')
        return render_template('login.html', error_text="Invalid username or password")
    else:
        if check_for_user():
            return render_template('home.html')
        return render_template('login.html')
@app.route('/search', methods=['post'])
def search():
    'Route to search'
    term = request.form.get('term', None)
    services = request.form.getlist('services', None)
    requestor = Requestor()
    if 'Twitter' in services:
        results = requestor.search_twitter(term)
        print(results)
        return render_template('home.html', results=results)
    #placeholder to ping the apis
    return render_template('home.html', results=list())
@app.route('/home')
@app.route('/home.html')
def home():
    '''search form'''
    if check_for_user():
        return render_template('home.html', results=list())
    return render_template('index.html')
@app.route('/signup', methods=['get', 'post'])
@app.route('/signup.html', methods=['get'])
def sign_up():
    'Sign up a new user'
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        first_name = request.form.get('first-name')
        last_name = request.form.get('last-name')
        print(first_name, last_name, username, password)
        user_manager = UserManager()
        try:
            user_manager.add_user(first_name, last_name, username, password)
            session['user'] = username
        except Exception as e:
            return render_template('signup.html', error_text="Unable to create user", header=render_template('header.html'))
        return render_template('home.html', header=render_template('headerLogged.html'))
    else:
        return render_template('signup.html', header=render_template('header.html'))
def check_for_user():
    '''check if a user has logged in, refresh the expiration
    if logged in, auto logout after 30 minutes of inactivity
    '''
    try:
        # will throw a KeyError if it doesn't exist
        _ = session['username']
        #will throw a ValueError if not a number
        expiration = float(session['expiration'])
        #get the current time in seconds
        current = time.time()
        #if the login has expired
        if current > expiration:
            #remove the user from the session
            session['username'] = None
            expiration = None
            return False
        else:
            #refresh the expiration to be 30 minutes from now
            session['expiration'] = current + (30 * 60)
            return True
    except KeyError:
        #if the username or expiration is not in the session
        return False
    except ValueError:
        #if the expiration is not a valid float
        return False
@app.route('/profile.html', methods=['get','post'])
def profile():
   return render_template('profile.html')

if __name__ == '__main__':
    app.run()
    