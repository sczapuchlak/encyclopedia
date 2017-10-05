'''Database Module'''
__author__ = 'Alex'
import sqlite3
from src.logger import Logger
#database class
class Database():
    '''Data Access Layer'''
    def __init__(self):
        self.sql_file = "encyclopediaDB"
        try:
            conn = self._get_connection()
            Logger.log("Connection to " + self.sql_file + " success!")
            curs = conn.cursor()
            #Users Table
            curs.execute('CREATE TABLE Users'
                 '(UserID INTEGER PRIMARY KEY AUTOINCREMENT ,'
                 'FirstName TEXT NOT NULL,'
                 'LastName TEXT NOT NULL,'
                 'EmailAddress TEXT NOT NULL,'
                 'UserName TEXT NOT NULL,'
                 'Password TEXT NOT NULL);')
            #UserSearch Table
            curs.execute('CREATE TABLE UserSearch'
                 '(SearchID INTEGER PRIMARY KEY AUTOINCREMENT,'
                 'SearchText TEXT NOT NULL,'
                 'UserID TEXT NOT NULL,'
                 'FOREIGN KEY(UserID) REFERENCES Users(UserID))')
            Logger.log("Table 'Users' Created Successfully!")
        except(sqlite3.OperationalError):
            Logger.log("Table already exists")
        conn.close()
    def get_user(self, username):
        '''gets user information based on the username'''
        conn = self._get_connection()
        curs = conn.cursor()
        curs.execute('SELECT UserID, (FirstName + LastName) as Name, UserName, EmailAddress FROM Users WHERE Username = "{un}"'.format(un=username))
        user = curs.fetchone()
        conn.close()
        return user
    def add_user(self, first_name, last_name, username, password):
        '''add_user method that takes in information name, username, and password to add a user to the Table Users'''
        conn = self._get_connection()
        curs = conn.cursor()
        curs.execute('INSERT INTO Users (FirstName, LastName, UserName, Password) VALUES(?,?,?,?)', (first_name, last_name, username, password))
        conn.commit()
        conn.close()
    def find_user_with_email(self, email):
        '''find_user_with_email method that takes the users email and returns the users information'''
        conn = self._get_connection()
        curs = conn.cursor()
        curs.execute('SELECT UserID, (FirstName + LastName) as Name, UserName, EmailAddress FROM Users WHERE EmailAdress = ?', (email))
        all_rows = curs.fetchall()
        conn.close()
        return all_rows
    def _get_connection(self):
        return sqlite3.connect(self.sql_file)
