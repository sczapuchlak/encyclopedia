import bcrypt


class UserManager():
    def __init__(self, database):
        self.database = database

    def add_user(self, first_name, last_name, username, password):
        password_hash = bcrypt.hash_password(password, bcrypt.get_salt())
        self.database.add_user(first_name, last_name, username, password_hash)

    def validate_credentials(self,username, password):
        user = self.database.get_user(username)
        db_hash = user[]
        user_hash = bcrypt.hash_password(password, bcrypt.get_salt())
        return user_hash == db_hash


    def hash_password(self, password):
            bcrypt.hashpw(password, bcrypt.gensalt())
