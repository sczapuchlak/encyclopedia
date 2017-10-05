'''User related activities'''
import bcrypt
from src.database import Database
from src.user import user

class UserManager():
    '''Manager the user's of this application'''
    def __init__(self):
        self.database = Database()
        self.user = user()

    def add_user(self, first_name, last_name, username, password):
        '''Add a user to the database'''
        password_hash = self._hash_password(password)
        self.database.add_user(first_name, last_name, username, password_hash)

    def findUser(self, first_name, last_name, username, password, email):
        '''looks for username and email'''
        user = self.database.get_user(username)
        mail = self.database.get_user(email)

        if user is not None:
            return self.user
        if mail is not None:
            return self.mail

    def validate_credentials(self, username, password):
        '''validate a password matches what is in the database'''
        user = self.database.get_user(username)
        if user is None:
            return False
        db_hash = user[4]
        user_hash = bcrypt.hashpw(password, db_hash)
        return user_hash == db_hash

    def _hash_password(self, password):
        return bcrypt.hashpw(password, bcrypt.gensalt())
