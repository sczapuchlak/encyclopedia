'''User related activities'''
import bcrypt
from src.database import Database
class UserManager():
    '''Manager the user's of this application'''
    def __init__(self):
        self.database = Database()
    def add_user(self, first_name, last_name, username, password):
        '''Add a user to the database'''
        password_hash = self._hash_password(password)
        self.database.add_user(first_name, last_name, username, password_hash)
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
