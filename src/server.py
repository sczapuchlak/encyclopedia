'''main entrypoint for the application'''
import time
from os import environ, path
from src.login import UserManager
from src.logger import Logger
from src.api import Requestor, Result
from flask import Flask, render_template, request, session, redirect, send_from_directory, jsonify
app = Flask(__name__, '/static', static_folder='../static', template_folder='../templates')
app.secret_key = 'rubber baby buggy bumbers'
app.config['DEBUG'] = environ.get('env') != 'PROD'
app.config['TEMPLATES_AUTO_RELOAD'] = app.config['DEBUG']


USER_MANAGER = UserManager()


@app.route('/')
@app.route('/index.html')
@app.route('/index', methods=['get'])
def index():
    'Main template route'
    if check_for_user():
        # make sure that we go to home if the user is logged in
        Logger.log('user exists sending home.html')
        return redirect('/home.html')
    Logger.log('user does not exist, returning index.html')
    return render_template('index.html')
@app.route('/login', methods=['post', 'get'])
@app.route('/login.html', methods=['get'])
def auth():
    'Authentication endpoint'
    # if the request is a post
    if request.method == 'POST':
        Logger.log('POST')
        # try and get the info entered
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        # check if the user exists and the password matches
        if USER_MANAGER.validate_credentials(username, password):
            Logger.log('user login valid')
            # log the user in with the session
            sign_user_in(username)
            # send the user to the home page
            return redirect('home.html')
        Logger.log('user login invalid')
        # send the user the login page with the error text
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
    # try and get the term
    term = request.form.get('term', None)
    # try and get the selected services as a list
    services = request.form.getlist('services', None)
    # add the search to the user's profile
    USER_MANAGER.add_search(session['username'], term, services)
    # initialize the api service
    requestor = Requestor()
    # create a blank result
    results = Result()
    # check for each of the available selected service
    if 'Twitter' in services:
        Logger.log('Twitter')
        results.tweets = requestor.search_twitter(term)
    if 'Giphy' in services:
        Logger.log('Giphy')
        results.gifs = requestor.search_giphy(term)
    if 'Wikipedia' in services:
        Logger.log('Wikipedia')
        results.articles = requestor.search_wiki(term)
    Logger.log('returning dict of results %s' % results)
    return render_template('home.html', results=results)
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
        try:
            USER_MANAGER.add_user(first_name, last_name, username, password, email)
            sign_user_in(username)
            Logger.log('user created')
        except RuntimeError as err:
            Logger.log('failed to create user')
            return render_template('signup.html', error_text=err.args[0])
        Logger.log('redirecting to home')
        return redirect('home.html')
    Logger.log('sending signup')
    return render_template('signup.html')
@app.route('/searches', methods=['get'])
def searches():
    '''get the search history for this user'''
    if check_for_user():
        username = session['username']
        Logger.log(username)
        user = USER_MANAGER.get_user_profile(username)
        Logger.log(user.searches)
        return jsonify(searches=list(map(lambda s: s.search_text, user.searches)))
    return jsonify(searches=list())
@app.route('/profile.html', methods=['get', 'post'])
def profile():
    '''get the user profile'''
    if request.method == 'GET':
        Logger.log('GET')
        if check_for_user():
            username = session['username']
            Logger.log(username)
            user = USER_MANAGER.get_user_profile(username)
            Logger.log(user)
            if user is None:
                return render_template('profile.html', error='Unable to find user')
            return render_template('profile.html', user=user)
    return redirect('/index.html')
@app.route('/signout', methods=['get'])
def signout():
    '''sign the current user out'''
    if check_for_user():
        Logger.log('user logged in, signing out')
        sign_user_out()
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
            sign_user_out()
            return False
        Logger.log('current is less than expiration, refreshing')
        #refresh the expiration to be 30 minutes from now
        add_expiration()
        return True
    except KeyError:
        Logger.log('No username in session')
        #if the username or expiration is not in the session
        return False
    except ValueError:
        Logger.log('expiration was not a valid float %s' % expiration)
        #if the expiration is not a valid float
        return False
def sign_user_in(username):
    '''add the required information to the session for a signed in user'''
    session['username'] = username
    add_expiration()
def add_expiration():
    '''Update or add the exxpiration to the session'''
    session['expiration'] = time.time() + (30 * 60)
def sign_user_out():
    '''remove the information from the session to sign a user out'''
    del session['username']
    del session['expiration']
@app.route('/favicon.ico', methods=['get'])
def favicon():
    '''route for the favicon'''
    Logger.log('')
    return send_from_directory(path.join(app.root_path, 'static', 'images'), 'favicon.ico',\
    mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run()
