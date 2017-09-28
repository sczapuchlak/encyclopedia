'''main entrypoint for the application'''
from flask import Flask, render_template, request, session
from src.twitterAPI import Requestor
app = Flask(__name__)
@app.route('/')
@app.route('/index.html')
@app.route('/index', methods=['get'])
def index():
    'Main template route'
    try:
        session['username']
        return render_template('home.html')
    except:
        return render_template('index.html')
@app.route('/login', methods=['post', 'get'])
@app.route('/login.html', methods=['get'])
def auth():
    'Authentication endpoint'
    if request.method == 'POST':
        try:
            username = request.form.get('username',None)
            password = request.form.get('password', None)
        except Exception as e:
            print('error getting values from from', e)
        #placeholder to validate password here
        #user_manager = UserManager()
        if True: #user_manager.validate_password(username, password)
            return render_template('index.html')
        return render_template('login.html', error_text="Invalid username or password")
    else:
        return render_template('login.html')
@app.route('/search', methods=['post'])
def search():
    'Route to search'
    term = request.form.get('term', None)
    services = request.form.getlist('services', None)
    requestor = Requestor()
    if 'Twitter' in services:
        results = requestor.search_twitter(term)
        return render_template('home.html', results=results)
    #placeholder to ping the apis
    return render_template('home.html', results=list())
@app.route('/home')
@app.route('/home.html')
def home():
    '''search form'''
    return render_template('home.html', results=list())
@app.route('/signup', methods=['get', 'post'])
@app.route('/signup.html', methods=['get'])
def sign_up():
    'Sign up a new user'
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        first_name = request.form.get('first-name')
        last_name = request.form.get('last-name')
        print(username, password, first_name, last_name)
        user_manager = None
        #try:
            #user_manager.add_user(username, password, first_name, last_name)
            #session['user'] = username
        #except Exception as e:
            #return render_template('signup.html', error_text="Unable to create user")
        return render_template('home.html')
    else:
        return render_template('signup.html')
