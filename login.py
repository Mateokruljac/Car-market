import time
from SignIN import SignIN
from Data import mycursor

class LogIn: 
    @classmethod
    def log_in(cls):
        print("LOG IN")
        cls.username = input("Username: ")
        cls.password = input("Password: ")            
        mycursor.execute(f"SELECT * FROM users WHERE username = '{cls.username}' AND password = '{cls.password}'")
        cls.myresult = mycursor.fetchone()
        if type(cls.myresult) == type(None):
            print("wait a few seconds")
            time.sleep(3)
            print("Invalid username or password!")
            print("*****************")
            print("Try again or create a new account!")
            print("1)Try again\n2) New account")
            userChoice = int(input("Select: "))
            if userChoice == 2:
                print("Create your new account")
                SignIN.sign_IN()
            if userChoice == 1:
                LogIn()
        
        else:
            cls.username == cls.myresult[3] and cls.password == cls.myresult[5]
            cls.userId = cls.myresult[0]
            print("wait a few seconds!")
            time.sleep(3)
            print("*****************")
       