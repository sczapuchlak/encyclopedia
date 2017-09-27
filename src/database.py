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
                 'Username TEXT NOT NULL,'
                 'Password TEXT NOT NULL);')

            print("Table 'Users' Created Successfully!")

        except(sqlite3.OperationalError):
            print("Table already exists")

    def add_user(self, name, username, password):
        self.curs.execute('INSERT INTO Users (UserName, Password) VALUES(?,?,?)', (name, username, password))
        self.conn.commit()
        self.conn.close()