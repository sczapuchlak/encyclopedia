__author__ = 'Alex'
import sqlite3

def create_DB():
    sqlFile = "encyclopediaDB"
    conn = sqlite3.connect(sqlFile)
    print("Connection to " + sqlFile + " success!")
    curs = conn.cursor()

    curs.execute('CREATE TABLE Users'
                 '(UserID INT PRIMARY KEY autoincrement,'
                 'Username TEXT NOT NULL,'
                 'Password TEXT NOT NULL)')