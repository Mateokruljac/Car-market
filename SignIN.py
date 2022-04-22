import mysql.connector
my_database = mysql.connector.connect(
    host = "localhost",   
    username = "root",
    password = "password",
    database = "pic"
)

mycursor = my_database.cursor()

class SignIN:
    def sign_IN(self):
        while True:
            self.first_name = input("Name: ")
            self.last_name = input("Surname: ")
            self.username = input("Username: ")
            self.email = input("Email: ")
            self.password = input("Password: ")
            self.city = input ("City: ")
            mycursor.execute("SELECT * FROM users")
            self.AllUsers = mycursor.fetchall()
            usernames = []
            emails = []
            for x in range (len(self.AllUsers)):
                usernames.append(self.AllUsers[x][3])
                emails.append (self.AllUsers[x][4])
            if self.username in usernames or self.email in emails:
                print("This username or email already exists!")
            else: 
                self.sql = "INSERT INTO users (first_name,last_name,username,email,password,city) VALUES (%s,%s,%s,%s,%s,%s)"
                self.userInfo = (self.first_name,self.last_name,self.username,self.email,self.password,self.city)
                mycursor.execute(self.sql,self.userInfo)
                my_database.commit()
                print(mycursor.rowcount,"user added!")
                break