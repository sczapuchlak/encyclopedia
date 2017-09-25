__author__ = 'Alex'
import sqlite3

class Users():
    def __init__(self):
        pass

    def addUsers(self, username, password):
        conn = sqlite3.connect("encyclopediaDB")
        curs = conn.cursor()
        curs.execute('INSERT INTO Users (UserName, Password) VALUES(?,?)', (username, password))
        conn.commit()
        conn.close()
