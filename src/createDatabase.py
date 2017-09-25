__author__ = 'Alex'
import sqlite3

def create_DB():
    sqlFile = "encyclopediaDB"
    conn = sqlite3.connect(sqlFile)
    print("Connection to " + sqlFile + " success!")
    curs = conn.cursor()

    try:
        curs.execute('CREATE TABLE Users'
                 '(UserID INTEGER PRIMARY KEY AUTOINCREMENT ,'
                 'Username TEXT NOT NULL,'
                 'Password TEXT NOT NULL);')

        print("Table 'Users' Created Successfully!")

    except(sqlite3.OperationalError):
        print("Table already exists")

def main():
    create_DB()

main()