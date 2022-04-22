from Data import mycursor,my_database
from login import LogIn

class Modify:
    def modify_car(self):
        print("Modify set car")
        print("*"*18)
        self.userId = LogIn.userId
        AllMyCars = f"SELECT * FROM cars WHERE user_id = {self.userId}"
        mycursor.execute(AllMyCars)
        self.UserCars =mycursor.fetchall()
        i = 0
        while i < len(self.UserCars):
            carID = (self.UserCars[i][0])
            car_year = (self.UserCars[i][3])
            car_fuel = (self.UserCars[i][4])
            car_km = (self.UserCars[i][5])
            car_engineVolume = (self.UserCars[i][5])
            print(f"id: {carID}")
            print(f"Year: {car_year}")
            print(f"Fuel: {car_fuel}")
            print(f"KM: {car_km}")
            print(f"Engine Volume: {car_engineVolume}")
            print("*"*18)
            i += 1 
        self.selectCar = int(input("Select car id: "))
        self.selectYear = int(input("Year: "))
        self.selectFuel = (input("Fuel: "))
        self.selectKm = int(input("Year: ")) 
        self.selectEngineVolume = int(input("Engine Volume: "))                       
        self.sql = f"UPDATE cars SET year = {self.selectYear}, fuel = '{self.selectFuel}', km = {self.selectKm}, engine_volume = '{self.selectEngineVolume}' WHERE id = {self.selectCar}"
        mycursor.execute(self.sql)
        my_database.commit()
        print("Executed successfully")