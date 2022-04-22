import mysql.connector
my_database = mysql.connector.connect(
    host = "localhost",   
    username = "root",
    password = "password",
    database = "pic"
)

mycursor = my_database.cursor()