from Data import mycursor

class Searching:
    def search (self):
        print("Check out our offer!")
        mycursor.execute("SELECT * FROM car_brands")
        self.brands = mycursor.fetchall()
        y = 1
        for x in range(len(self.brands)):
            print(f"{y}. {self.brands[x][1]}")
            y +=1
        user_choice = int(input("Select a car: "))        
        mycursor.execute(f"SELECT * FROM cars WHERE brand_id = {user_choice}")
        self.all_cars = mycursor.fetchall()
        print(f"Found: {len(self.all_cars)} car(s).")
        for i in range(len(self.all_cars)):
            print("*****************")
            print("Name :",self.all_cars[i][2])
            print("Year :",self.all_cars[i][3])
            print("Fuel :",self.all_cars[i][4])
            print("Km :",self.all_cars[i][5])
            print("Engine volume :",self.all_cars[i][6])
            print("-"*18)
            