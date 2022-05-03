from Data import mycursor,my_database
from login import LogIn
import time

class SetCar:
    def set_car(self):
        print("Loading...")
        time.sleep(2)
        self.user_Id = LogIn.userId
        self.brands = "SELECT * FROM car_brands"
        mycursor.execute(self.brands)
        self.brandsResult = mycursor.fetchall()
        print("Choose the brand of your car!")
        y = 1
        for x in self.brandsResult:
            print(f"{y}.",x[1])
            y += 1
        self.userSelect = int (input("Please, select Your car :"))
        self.name = input("Name : ")
        try:
            self.km = int(input("Km : "))
        except TypeError:
            print("Please forward integer!")
            self.km = int(input("Km : "))
        self.engineVolume = int(input("Engine volume : "))
        self.year = int(input("Year : "))
        self.fuel = input("Fuel : ")
        
        self.carKeys = "INSERT INTO cars(brand_id,name,year,fuel,km,engine_volume,user_id) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        self.carValue = (self.userSelect,self.name,self.year,self.fuel,self.km,self.engineVolume,self.user_Id)
        mycursor.execute(self.carKeys,self.carValue)
        my_database.commit()
        print(mycursor.rowcount,"car set!")
