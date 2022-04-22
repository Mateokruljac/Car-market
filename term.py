from login import LogIn
from Data import my_database,mycursor

class Term: 
    def search_term (self):
        print("Welcome to 'Search term'!")
        userInput = input ("User input (car name, fuel).Use the first capital letter: ")
        self.userInput = userInput.capitalize()
        sql = f"SELECT * FROM cars WHERE name LIKE '%{self.userInput}%' OR  fuel LIKE '%{self.userInput}%' OR km LIKE '%{self.userInput}%'"
        mycursor.execute(sql)
        self.Result = mycursor.fetchall()
        i = 0
        while i < len(self.Result):
            car_name = (self.Result[i][2])
            car_year = (self.Result[i][3])
            car_fuel = (self.Result[i][4])
            car_km = (self.Result[i][5])
            car_engineVolume = (self.Result[i][5])
            print(f"Name: {car_name}")
            print(f"Year: {car_year}")
            print(f"Fuel: {car_fuel}")
            print(f"KM: {car_km}")
            print(f"Engine Volume: {car_engineVolume}")
            print("*"*18)
            i += 1
        
   