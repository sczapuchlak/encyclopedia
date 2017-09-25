import sqlite3

def askUser():
    userOption = 3
    while userOption != 0:
        options(askUser)
        userOption = int(input("What would you like to select?"))
        if userOption == 1:
            print("----------Create a new account-----------")
            username = input("Create a username: ")
            password = input("Create a password: ")
        if userOption == 2:
            print("---------Login-----------")
            input1 = " "
            input2 = " "
            while input1 != username:
                input1 = input("Enter your username: ")
            if input1 != username:
                print("Not a valid username!")
            while input2 != password:
                input2 = input("Enter your password: ")
            if input2 != password:
                print("The password is incorrect!")
            if input2 == password:
                print("Welcome back!")
        if userOption == 3:
            exit()

def options(self):
    option1 = "1)Create an account"
    option2 = "2)Login"
    option3 = "3)Exit"

    print("What would you like to do?:\nOptions:\n",option1+"\n",option2+"\n",option3)

askUser()


class AddUser():
    def __init__(self):
        pass

    def add(self, cursor, connection, username, password):
        user = username
        pwd = password

        try:
            cursor.execute("INSERT INTO TABLE (user, pwd))\
                           VALUES ("+str(user)+", "+str(pwd)+")")
            connection.commit()
        except sqlite3.IntegrityError:
            print("Username already exists!")