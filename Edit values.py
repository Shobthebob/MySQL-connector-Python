import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root" , password="shob25" , database="test")

mycursor = mydb.cursor( )
sql = "UPDATE accounts SET Username='SUP BRO' WHERE Passcode='Password!123'"
# Can also do vice versa 
# sql = "UPDATE accounts SET Passcode='Never gonna give you up' WHERE Username='Shob'"

mycursor.execute(sql)
mydb.commit( )