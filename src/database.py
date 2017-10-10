'''Database Module'''
__author__ = 'Alex'
import sqlite3

#database class
class Database():
    '''Data Access Layer'''
    def __init__(self):
        self.sql_file = "encyclopedia.sqlite3"
        self._try_create_tables()
    def get_user(self, username):
        '''gets user information based on the username'''
        conn = self._get_connection()
        curs = conn.cursor()
        curs.execute('SELECT UserID, FirstName, LastName, UserName, EmailAddress, password FROM Users WHERE Username = "{un}"'.format(un=username))
        user = curs.fetchone()
        conn.close()
        print(user)
        return user
    def add_user(self, first_name, last_name, username, password, email):
        '''add_user method that takes in information name, username, and password to add a user to the Table Users'''
        conn = self._get_connection()
        curs = conn.cursor()
        curs.execute('''INSERT INTO Users 
                        (FirstName, LastName, UserName, Password, EmailAddress)
                        VALUES("{fn}","{ln}","{un}","{pw}","{em}")'''\
                        .format(fn=first_name, ln=last_name, un=username, pw=password, em=email))
        conn.commit()
        conn.close()
    def find_user_with_email(self, email):
        '''find_user_with_email method that takes the users email and returns the users information'''
        conn = self._get_connection()
        curs = conn.cursor()
        curs.execute('SELECT UserID, FirstName, LastName, UserName, EmailAddress, password FROM Users WHERE EmailAddress = "{em}"'.format(em=email))
        all_rows = curs.fetchone()
        conn.close()
        return all_rows
    def _get_connection(self):
        return sqlite3.connect(self.sql_file)
    def _try_create_tables(self):
        try:
            conn = self._get_connection()
            print("Connection to " + self.sql_file + " success!")
            curs = conn.cursor()
            #Users Table
            curs.execute('''CREATE TABLE Users
                 (UserID INTEGER PRIMARY KEY AUTOINCREMENT ,
                 FirstName TEXT NOT NULL,
                 LastName TEXT NOT NULL,
                 EmailAddress TEXT NOT NULL,
                 UserName TEXT NOT NULL,
                 Password TEXT NOT NULL);''')
            #UserSearch Table
            print("Table 'Users' Created Successfully!")
            curs.execute('''CREATE TABLE UserSearch
                 (SearchID INTEGER PRIMARY KEY AUTOINCREMENT,
                 SearchText TEXT NOT NULL,
                 UserID TEXT NOT NULL,
                 FOREIGN KEY(UserID) REFERENCES Users(UserID))''')
            print('Table UserSearch created successfully!')
        except(sqlite3.OperationalError):
            print("Tables already exists")
        conn.close()
if __name__ == '__main__':
    _ = Database()
