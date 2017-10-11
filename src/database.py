'''Database Module'''
import sqlite3
from src.user import User
from src.userSearch import UserSearch
from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import mapper, sessionmaker
METADATA = MetaData()
#database class
class Database():
    '''Data Access Layer'''
    def __init__(self, connection_string='sqlite:///test.sqlite3'):
        self.sql_file = connection_string
        self.users = self._map_users()
        self.user_searches = self._map_user_searches()
        self.engine = self._get_connection()
        METADATA.create_all(self.engine)
        #old: self._try_create_tables()

#-------------------------------------NEW CODE FOR ORM-------------------------------------------
    def add_user(self, user):
        session = self._get_session()
        session.add(user)
        session.commit()
    def get_user(self, username):
        session = self._get_session()
        for user in session.query(User).\
            filter(User.user_name==username):
            return user
    def find_user_with_email(self, email):
        session = self._get_session()
        for user in session.query(User).\
            filter(User.user_name==email):
            return user
    def _map_users(self):
        users = Table('Users', METADATA,\
            Column('user_id', Integer, primary_key=True),
            Column('first_name', String),\
            Column('last_name', String),\
            Column('user_name', String),\
            Column('password', String),\
            Column('email_address', String))
        mapper(User, users)
        return users
    def _map_user_searches(self):
        user_searches = Table('UserSearches', METADATA,\
            Column('search_id', Integer, primary_key=True),
            Column('search_text', String),\
            Column('user_id', Integer))
        mapper(UserSearch, user_searches)
        return user_searches
    def _get_connection(self):
        engine = create_engine(self.sql_file)
        return engine
    def _get_session(self):
        Session = sessionmaker(bind=self.engine)
        return Session()
if __name__ == '__main__':
    _ = Database()
