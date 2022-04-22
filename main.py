from term import Term
from Delete import Delete
from modify import Modify
from SignIN import SignIN
from login  import LogIn
from Searching import Searching
from Setcar import SetCar
from Userprofile import UserProfile

# while True:
print("Welcome to PIC!")
print("1) Sign In")
print("2) Log in")

            
try: 
    user_input = int(input("Choice: "))
except ValueError:
    print("Please use integer!")
    user_input = int(input("Choice: "))
    
if user_input == 1:
    SignIN().sign_IN()
if user_input == 2:
    LogIn().log_in()
    print("Welcome to Car Market!")
    print("Select one : ")
    print("*****************")
    print("1) Search cars : ")
    print("2) Set up a car : ")
    print("3) Your profile : ")
    print("4) Modify a set car : ")
    print("5) Delete a car : ")
    print("6) Search (name,fuel...) : ")
    print("*****************")
    user_choice = int(input("Select one: "))
    if user_choice == 1:
        Searching().search()
    if user_choice == 2: 
        SetCar().set_car()
    if user_choice == 3:
        UserProfile().message()
    if user_choice == 4: 
        Modify().modify_car()
    if user_choice == 5: 
        Delete().delete_car()
    if user_choice == 6: 
        Term().search_term()
     