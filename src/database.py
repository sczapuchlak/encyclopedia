'''Database Module'''
import sqlite3
from src.user import User
from src.userSearch import UserSearch
from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, create_engine
import sqlalchemy.types as types
from sqlalchemy.orm import mapper, sessionmaker, relationship
#database class
class Database():
    '''Data Access Layer'''
    def __init__(self, connection_string='sqlite:///media.cheetah.sqlite3'):
        self.sql_file = connection_string
        self.engine = self._get_connection()
        self.metadata = MetaData(bind=self.engine)
        try:
            self.users, self.user_searches = self._create_tables()
            self._map_user_searches()
            self._map_users()
        except Exception as e:
            print(e)
        #old: self._try_create_tables()

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
            filter(User.email_address==email):
            return user
    def add_search(self, search):
        session = self._get_session()
        session.add(search)
        session.commit()
    def get_searches_for_user(self, user_id):
        session = self._get_session()
        return session.query(UserSearch).filter(UserSearch.user_id == user_id).all()
    def _create_tables(self):
        users = Table('Users', self.metadata,\
            Column('user_id', Integer, primary_key=True),
            Column('first_name', String),\
            Column('last_name', String),\
            Column('user_name', String),\
            Column('password', String),\
            Column('email_address', String))
        users.create(self.engine, checkfirst=True)
        user_searches = Table('UserSearches', self.metadata,\
            Column('search_id', Integer, primary_key=True),
            Column('search_text', String),\
            Column('services', Services),\
            Column('user_id', Integer, ForeignKey('Users')))
        user_searches.create(self.engine, checkfirst=True)
        return (users, user_searches)
    def _map_users(self):
        try:
            mapper(User, self.users, properties={
                'searches': relationship(UserSearch, backref="Users")
            })
        except:
            pass
    def _map_user_searches(self):
        try:
            mapper(UserSearch, self.user_searches)
        except:
            pass
    def _get_connection(self):
        engine = create_engine(self.sql_file)
        return engine
    def _get_session(self):
        Session = sessionmaker(bind=self.engine)
        return Session()


class Services(types.TypeDecorator):
    impl = types.Integer

    def process_bind_param(self, value, dialect):
        ret = 0
        for service in value:
            if service.lower() == 'twitter':
                ret += 1
            if service.lower() == 'giphy':
                ret += 2
            if service.lower() == 'flickr':
                ret += 4
        return ret
    def process_result_value(self, value, dialect):
        ret = list()
        if value & 1 > 0:
            ret.append('twitter')
        if value & 2 > 0:
            ret.append('giphy')
        if value & 4 > 0:
            ret.append('flickr')
        return ret

if __name__ == '__main__':
    _ = Database()

