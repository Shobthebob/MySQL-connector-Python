import mysql.connector

mydb = mysql.connector.connect(host="", user="" , password="")

mycursor = mydb.cursor( )

mycursor.execute("CREATE DATABASES test")

for db in mycursor:
	print(db)

