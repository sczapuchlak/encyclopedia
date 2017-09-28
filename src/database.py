__author__ = 'Alex'
import sqlite3

#database class
class Database():
    #Database Constructor
    def __init__(self):
        self.sqlFile = "encyclopediaDB"
        self.conn = sqlite3.connect(self.sqlFile)
        print("Connection to " + self.sqlFile + " success!")
        self.curs = self.conn.cursor()
        try:
            self.curs.execute('CREATE TABLE Users'
                 '(UserID INTEGER PRIMARY KEY AUTOINCREMENT ,'
                 'FirstName TEXT NOT NULL,'
                 'LastName TEXT NOT NULL,'
                 'UserName TEXT NOT NULL,'
                 'Password TEXT NOT NULL);')

            print("Table 'Users' Created Successfully!")

        except(sqlite3.OperationalError):
            print("Table already exists")

    #gets user information based on the username
    def get_user(self, username):
        self.curs.execute('SELECT * FROM Users WHERE Username = (?)', (username))

    #add_user method that takes in information name, username, and password to add a user to the Table Users
    def add_user(self, name, username, password):
        firstName,lastName = name.split(" ")

        self.curs.execute('INSERT INTO Users (FirstName, LastName, UserName, Password) VALUES(?,?,?,?)', (firstName, lastName, username, password))
        self.conn.commit()
        self.conn.close()