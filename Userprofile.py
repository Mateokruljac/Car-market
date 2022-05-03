from Data import my_database,mycursor
from login import LogIn
class UserProfile: 
    def message(self):
        print ("Welcome to mailbox.")
        self.userId = LogIn.userId
        self.messages = f"SELECT * FROM messages WHERE user_received_id = {self.userId}"
        mycursor.execute(self.messages)
        self.messagesResult = mycursor.fetchall()
        if self.messagesResult:
            for x in self.messagesResult:# možemo prmiti više poruka
                self.carId = self.messagesResult[0][1]
                self.sender = f"SELECT id,first_name,last_name FROM users WHERE id = {x[2]}" #x[2] -> primjera radi
                mycursor.execute(self.sender)
                self.senderResult = mycursor.fetchall()
                print(self.senderResult)
                self.senderID = self.senderResult[0][0]
                print(f"Message from : ",self.senderResult[0][1],self.senderResult[0][2])#name and surname
                print(f"Message : ",x[4]) # 4 ide jer je poruka na 4. poziciji u tabeli message
                print("*"*18)
                self.answer = input ("If you want to answer, just type yes:")
                if self.answer.strip().lower() == "yes":
                    message = input("Answer: ")                           
                    self.carID = f"INSERT INTO messages (car_id,user_sent_id,user_received_id,message) VALUES ({self.carId},{self.userId},{self.senderID},'{message}')" #obavezno  ' ' navodnici
                    mycursor.execute(self.carID)
                    my_database.commit()
                    print(mycursor.rowcount,"executed!")
