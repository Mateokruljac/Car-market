from login import LogIn
from Data import mycursor,my_database

class Delete: 
    def delete_car(self):
        print("Delete a car!")
        print("*"*18)
        self.userId = LogIn.userId
        self.AllMyCars = f"SELECT * FROM cars WHERE user_id = {self.userId}"
        mycursor.execute(self.AllMyCars)
        self.UserCars = mycursor.fetchall()     
        i = 0
        while i < (len(self.UserCars)):
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
        selectCar = input("Select car: ")
        self.sql = f"DELETE FROM cars WHERE id = {selectCar}"
        mycursor.execute(self.sql)
        my_database.commit()
        print("Successfully delete!")
    