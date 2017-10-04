'''Database Module'''
__author__ = 'Alex'
import sqlite3

#database class
class Database():
    '''Data Access Layer'''
    def __init__(self):
        self.sql_file = "encyclopediaDB"
        self.conn = sqlite3.connect(self.sql_file)
        print("Connection to " + self.sql_file + " success!")
        self.curs = self.conn.cursor()
        try:
            #Users Table
            self.curs.execute('CREATE TABLE Users'
                 '(UserID INTEGER PRIMARY KEY AUTOINCREMENT ,'
                 'FirstName TEXT NOT NULL,'
                 'LastName TEXT NOT NULL,'
                 'UserName TEXT NOT NULL,'
                 'Password TEXT NOT NULL);')

            #UserSearch Table
            self.curs.execute('CREATE TABLE UserSearch'
                 '(SearchID INTEGER PRIMARY KEY AUTOINCREMENT,'
                 'SearchText TEXT NOT NULL,'
                 'UserID TEXT NOT NULL,'
                 'FOREIGN KEY(UserID) REFERENCES Users(UserID))')
            print("Table 'Users' Created Successfully!")

        except(sqlite3.OperationalError):
            print("Table already exists")
    def get_user(self, username):
        '''gets user information based on the username'''
        curs = self._get_cursor()
        curs.execute('SELECT * FROM Users WHERE Username = "{un}"'.format(un=username))
        user = curs.fetchone()
        self.conn.close()
        return user
    def add_user(self, first_name, last_name, username, password):
        '''add_user method that takes in information name, username, and password to add a user to the Table Users'''
        curs = self._get_cursor()
        curs.execute('INSERT INTO Users (FirstName, LastName, UserName, Password) VALUES(?,?,?,?)', (first_name, last_name, username, password))
        self.conn.commit()
        self.conn.close()
    def _get_cursor(self):
        self.conn = sqlite3.connect(self.sql_file)
        return self.conn.cursor()