import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root" , password="")

mycursor = mydb.cursor( )

mycursor.execute("CREATE DATABASES test")

for db in mycursor:
	print(db)

