'''User related activities'''
import bcrypt
from src.database import Database
from src.user import User
from src.userSearch import UserSearch
class UserManager():
    '''Manager the user's of this application'''
    def __init__(self):
        self.database = Database()

    def add_user(self, first_name, last_name, username, password, email):
        '''Add a user to the database'''
        if self.find_user(username, email) is None:
            password_hash = self._hash_password(password)
            user = User(first_name, last_name, username, email, password=password_hash)
            self.database.add_user(user)
        else:   
            raise RuntimeError('User already exists')
    def find_user(self, username, email=''):
        '''looks for username and email'''
        user = self.database.get_user(username)
        if user is not None:
            return user
        return self.database.find_user_with_email(email)

    def validate_credentials(self, username, password):
        '''validate a password matches what is in the database'''
        user = self.database.get_user(username)
        if user is None:
            return False
        db_hash = user.password
        user_hash = bcrypt.hashpw(password, db_hash)
        return user_hash == db_hash
    def get_user_profile(self, username):
        '''get the user info from the db'''
        user = self.database.get_user(username)
        return user
    def add_search(self, username, term, services):
        '''add a search to the user's profile'''
        if username is None or\
        services is None or\
        term is None or\
        len(services) < 1:
            return
        user = self.database.get_user(username)
        self.database.add_search(UserSearch(None, term, services, user.user_id ))
    def _hash_password(self, password):
        return bcrypt.hashpw(password, bcrypt.gensalt())
