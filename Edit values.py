import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root" , password="" , database="")

mycursor = mydb.cursor( )
query = "UPDATE accounts SET Username='SUP BRO' WHERE Passcode='Password!123'"

mycursor.execute(query)
mydb.commit( )
