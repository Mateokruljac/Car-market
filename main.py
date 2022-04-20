import time 
import mysql.connector

myconnector = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "pic")
mycursor = myconnector.cursor()
print("""Welcome to pic""")
print("*****************")
print("SELECT:\n1) login\n2) sign in")

class LogSignIn:
    def logIn (self):
        print("*****************")
        print("LOG IN")
        mycursor.execute("SELECT * FROM users")
        myresult = mycursor.fetchall()
        self.username = input("Username: ")
        self.password = input("Password: ")
        usernames = []
        passwords = []
        for x in range (len(myresult)):
            usernames.append(myresult[x][3])
            passwords.append(myresult[x][5])
        
        for i in range (len(usernames)):
            if self.username == usernames[i] and self.password == passwords[i]:
                userId = myresult[i][0]
                print("wait a few seconds!")
                time.sleep(3)
                print("*****************")
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
                user_choice = int(input("Select : "))
                if user_choice == 1:
                    print("Check out our offer: ")
                    brands = "SELECT * FROM car_brands"
                    mycursor.execute(brands)
                    brandsResult = mycursor.fetchall()
                    print("Choose the brand of your car!")
                    y = 1
                    for x in brandsResult:
                        print(f"{y}.",x[1])
                        y += 1
                    YourChoice = input("Your choice: ")
                    cars =f"SELECT * FROM cars WHERE brand_id ={YourChoice}"
                    mycursor.execute(cars)
                    choosenCar = mycursor.fetchall()
                    print(f"Found: {len(choosenCar)} car(s).")
                    for i in range(len(choosenCar)):
                        print("*****************")
                        print("Name :",choosenCar[i][2])
                        print("Year :",choosenCar[i][3])
                        print("Fuel :",choosenCar[i][4])
                        print("Km :",choosenCar[i][5])
                        print("Engine volume :",choosenCar[i][6])
                        print("-"*18)
                    exit()    
                if user_choice == 2:
                    print("Loading...")
                    time.sleep(2)
                    brands = "SELECT * FROM car_brands"
                    mycursor.execute(brands)
                    brandsResult = mycursor.fetchall()
                    print("Choose the brand of your car!")
                    y = 1
                    for x in brandsResult:
                        print(f"{y}.",x[1])
                        y += 1
                    userSelect = int (input("Please, select Your car :"))
                    name = input("Name : ")
                    try:
                        km = int(input("Km : "))
                    except TypeError:
                        print("Please forward integer!")
                        km = int(input("Km : "))
                    engineVolume = int(input("Engine volume : "))
                    year = int(input("Year : "))
                    fuel = input("Fuel : ")
                    
                    self.carKeys = "INSERT INTO cars(brand_id,name,year,fuel,km,engine_volume,user_id) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                    self.carValue = (userSelect,name,year,fuel,km,engineVolume,userId)
                    mycursor.execute(self.carKeys,self.carValue)
                    myconnector.commit()
                    print(mycursor.rowcount,"car set!")
                    exit()
                
                if user_choice == 3:
                    print("*"*18)
                    print ("Welcome to mailbox.")
                    messages = f"SELECT * FROM messages WHERE user_received_id = {userId}"
                    mycursor.execute(messages)
                    messagesResult = mycursor.fetchall()
                    if messagesResult:
                        for x in messagesResult:# možemo prmiti više poruka
                            carId = messagesResult[0][1]
                            sender = f"SELECT id,first_name,last_name FROM users WHERE id = {x[2]}" #x[2] -> primjera radi
                            mycursor.execute(sender)
                            senderResult = mycursor.fetchall()
                            print(senderResult)
                            senderID = senderResult[0][0]
                            print(f"Message from : ",senderResult[0][1],senderResult[0][2])#name and surname
                            print(f"Message : ",x[4]) # 4 ide jer je poruka na 4. poziciji u tabeli message
                            print("*"*18)
                            answer = input ("If you want to answer, just type yes:")
                            if answer.strip().lower() == "yes":
                                message = input("Answer: ")                            # izbacio mi je error jer nije zatovrena zagrada!!!!PAZIIIII!!!!!!!
                                carID = f"INSERT INTO messages (car_id,user_sent_id,user_received_id,message) VALUES ({carId},{userId},{senderID},'{message}')" #obavezno  ' ' navodnici
                                mycursor.execute(carID)
                                myconnector.commit()
                                print(mycursor.rowcount,"executed!")
                    exit()
                if user_choice == 4:
                    print("Modify set car")
                    print("*"*18)
                    AllMyCars = f"SELECT * FROM cars WHERE user_id = {userId}"
                    mycursor.execute(AllMyCars)
                    UserCars =mycursor.fetchall()
                    i = 0
                    while i < len(UserCars):
                        carID = (UserCars[i][0])
                        car_year = (UserCars[i][3])
                        car_fuel = (UserCars[i][4])
                        car_km = (UserCars[i][5])
                        car_engineVolume = (UserCars[i][5])
                        print(f"id: {carID}")
                        print(f"Year: {car_year}")
                        print(f"Fuel: {car_fuel}")
                        print(f"KM: {car_km}")
                        print(f"Engine Volume: {car_engineVolume}")
                        print("*"*18)
                        i += 1 
                    selectCar = int(input("Select car id: "))
                    selectYear = int(input("Year: "))
                    selectFuel = (input("Fuel: "))
                    selectKm = int(input("Year: ")) 
                    selectEngineVolume = int(input("Engine Volume: "))                       
                    sql = f"UPDATE cars SET year = {selectYear}, fuel = '{selectFuel}', km = {selectKm}, engine_volume = '{selectEngineVolume}' WHERE id = {selectCar}"
                    mycursor.execute(sql)
                    myconnector.commit()
                    print("Executed successfully")
                    break
                if user_choice == 5:
                    print("Delete a car!")
                    print("*"*18)
                    AllMyCars = f"SELECT * FROM cars WHERE user_id = {userId}"
                    mycursor.execute(AllMyCars)
                    UserCars = mycursor.fetchall()     
                    i = 0
                    while i < (len(UserCars)):
                        carID = (UserCars[i][0])
                        car_year = (UserCars[i][3])
                        car_fuel = (UserCars[i][4])
                        car_km = (UserCars[i][5])
                        car_engineVolume = (UserCars[i][5])
                        print(f"id: {carID}")
                        print(f"Year: {car_year}")
                        print(f"Fuel: {car_fuel}")
                        print(f"KM: {car_km}")
                        print(f"Engine Volume: {car_engineVolume}")
                        print("*"*18)
                        i += 1 
                    selectCar = input("Select car: ")
                    sql = f"DELETE FROM cars WHERE id = {selectCar}"
                    mycursor.execute(sql)
                    myconnector.commit()
                    print("Successfully delete!")
                
                if user_choice == 6:
                    userInput = input ("User input (car name, fuel).Use the first capital letter: ")
                    sql = f"SELECT * FROM cars WHERE name LIKE '%{userInput}%' OR  fuel LIKE '%{userInput}%' OR km LIKE '%{userInput}%'"
                    mycursor.execute(sql)
                    Result = mycursor.fetchall()
                    i = 0
                    while i < len(Result):
                        car_name = (Result[i][2])
                        car_year = (Result[i][3])
                        car_fuel = (Result[i][4])
                        car_km = (Result[i][5])
                        car_engineVolume = (Result[i][5])
                        print(f"Name: {car_name}")
                        print(f"Year: {car_year}")
                        print(f"Fuel: {car_fuel}")
                        print(f"KM: {car_km}")
                        print(f"Engine Volume: {car_engineVolume}")
                        print("*"*18)
                        i += 1
                
                if user_choice == 7:
                    print("Shoppping!")
                    print("Check out our offer: ")
                    brands = "SELECT * FROM car_brands"
                    mycursor.execute(brands)
                    brandsResult = mycursor.fetchall()
                    print("Choose the brand of your car!")
                    y = 1
                    for x in brandsResult:
                        print(f"{y}.",x[1])
                        y += 1
                    YourChoice = input("Your choice: ")
                    cars =f"SELECT * FROM cars WHERE brand_id ={YourChoice}"
                    mycursor.execute(cars)
                    choosenCar = mycursor.fetchall()
                    print(f"Found: {len(choosenCar)} car(s).")
                    for i in range(len(choosenCar)):
                        print("*****************")
                        print("id:",choosenCar[i][0])
                        print("Name :",choosenCar[i][2])
                        print("Year :",choosenCar[i][3])
                        print("Fuel :",choosenCar[i][4])
                        print("Km :",choosenCar[i][5])
                        print("Engine volume :",choosenCar[i][6])
                        print("-"*18)
                    
                    print("Select the car!")
                    print("to be continued!...")
                           
        else:
            print("wait a few seconds")
            time.sleep(3)
            print("Invalid username or password!")
            print("*****************")
            print("Try again or create a new account!")
            print("1)Try again\n2) New account")
            userChoice = int(input("Select: "))
            if userChoice == 2:
                print("Create your new account")
                self.signIn()
            if userChoice == 1:
                self.logIn()
        
    def signIn (self):
        
        while True:
            print("SIGN IN")
            global first_name,last_name,username,email,password,city
            first_name = input ("Name: ")
            last_name = input ("Surname: ")
            username = input ("Username: ")
            email = input ("Email: ")
            password = input ("Password: ")
            city = input("City: ")
            username = username.lower()
            mycursor.execute("SELECT * FROM users")
            myresult = mycursor.fetchall()
            usernames = []
            emails = []
            for x in range (len(myresult)):
                usernames.append(myresult[x][3])
                emails.append(myresult[x][4])
            if username in usernames or email in emails:
                print("Select new username or email!")
            else:  
                self.sql = "INSERT INTO users (first_name,last_name,username,email,password,city) VALUES (%s,%s,%s,%s,%s,%s)"
                self.value = (first_name,last_name,username,email,password,city)
                mycursor.execute(self.sql,self.value)
                myconnector.commit()
                print("Successfully registered!")
                print(mycursor.rowcount,"user created!")
                break
                                   
    def option (self,your_option):
        if your_option == 1:
            self.logIn()
        if your_option == 2:
            self.signIn()
            
lsi = LogSignIn()
try:
    your_option = int(input("Select the number: "))
    lsi.option(your_option)
except ValueError: 
    print("Please, use integer!")
    your_option = int(input("Select the number: "))
    lsi.option(your_option)




    
        