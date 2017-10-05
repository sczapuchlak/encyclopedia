'''main entrypoint for the application'''
import time
from os import environ
from src.twitterAPI import Requestor
from src.login import UserManager
from src.logger import Logger
from flask import Flask, render_template, request, session, redirect
app = Flask(__name__, '/static', static_folder='../static', template_folder='../templates')
app.secret_key = 'rubber baby buggy bumbers'
app.config['DEBUG'] = environ.get('env') != 'PROD'
app.config['TEMPLATES_AUTO_RELOAD'] = app.config['DEBUG']

@app.route('/')
@app.route('/index.html')
@app.route('/index', methods=['get'])
def index():
    'Main template route'
    Logger.log('index %s' % session)
    if check_for_user():
        Logger.log('user exists sending home.html')
        return redirect('/home.html')
    Logger.log('user does not exist, returning index.html')
    return render_template('index.html')
@app.route('/login', methods=['post', 'get'])
@app.route('/login.html', methods=['get'])
def auth():
    'Authentication endpoint'
    if request.method == 'POST':
        Logger.log('POST')
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        user_manager = UserManager()
        if user_manager.validate_credentials(username, password):
            Logger.log('user login valid')
            session['username'] = username
            session['expiration'] = time.time() + (30 * 60)
            return redirect('home.html')
        Logger.log('user login invalid')
        return render_template('login.html', error_text="Invalid username or password")
    else:
        Logger.log('GET')
        if check_for_user():
            Logger.log('User is logged in, sending to home')
            return redirect('home.html')
        Logger.log('User is not logged in, sending to login page')
        return render_template('login.html')
@app.route('/search', methods=['post'])
def search():
    'Route to search'
    term = request.form.get('term', None)
    services = request.form.getlist('services', None)
    requestor = Requestor()
    if 'Twitter' in services:
        Logger.log('Twitter')
        results = requestor.search_twitter(term)
        Logger.log(results)
        return render_template('home.html', results=results)
    return render_template('home.html', results=list())
@app.route('/home')
@app.route('/home.html')
def home():
    '''search form'''
    if check_for_user():
        Logger.log('user logged in, sending to home')
        return render_template('home.html', results=list())
    Logger.log('user not logged in, sending to index')
    return redirect('index.html')
@app.route('/signup', methods=['get', 'post'])
@app.route('/signup.html', methods=['get'])
def sign_up():
    'Sign up a new user'
    if request.method == 'POST':
        Logger.log('POST')
        username = request.form.get('username')
        password = request.form.get('password')
        first_name = request.form.get('first-name')
        last_name = request.form.get('last-name')
        email = request.form.get('email')
        user_manager = UserManager()
        try:
            user_manager.add_user(first_name, last_name, username, password)
            session['username'] = username
            Logger.log('user created')
        except Exception as e:
            Logger.log('failed to create user')
            return render_template('signup.html', error_text="Unable to create user")
        Logger.log('redirecting to home')
        return redirect('home.html')
    else:
        Logger.log('sending signup')
        return render_template('signup.html')
@app.route('/profile.html', methods=['get','post'])
def profile():
    if check_for_user():
        return render_template('profile.html')
    return redirect('/index.html')
@app.route('/signout', methods=['get'])
def signout():
    '''sign the current user out'''
    if check_for_user():
        Logger.log('user logged in, signing out')
        del session['username']
        del session['expiration']
    Logger.log('redirecting to index')
    return redirect('/')
def check_for_user():
    '''check if a user has logged in, refresh the expiration
    if logged in, auto logout after 30 minutes of inactivity
    '''
    Logger.log('checking for user')
    try:
        # will throw a KeyError if it doesn't exist
        session_username = session['username']
        Logger.log('session_username %s' % session_username)
        #will throw a ValueError if not a number
        expiration = float(session['expiration'])
        Logger.log('session_expiration %s' % expiration)
        #get the current time in seconds
        current = time.time()
        Logger.log('current time %s' % current)
        #if the login has expired
        if current > expiration:
            Logger.log('current is greater than expiration, removing')
            #remove the user from the session
            del session['username']
            del session['expiration']
            return False
        else:
            Logger.log('current is less than expiration, refreshing')
            #refresh the expiration to be 30 minutes from now
            session['expiration'] = current + (30 * 60)
            return True
    except KeyError:
        Logger.log('No username in session')
        #if the username or expiration is not in the session
        return False
    except ValueError:
        Logger.log('expiration was not a valid float %s' % expiration)
        #if the expiration is not a valid float
        return False

if __name__ == '__main__':
    app.run()
