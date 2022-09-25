import mysql.connector

chetan = mysql.connector.connect(host="localhost", user="root" , password="shob25")

mycursor = chetan.cursor( )

mycursor.execute("CREATE DATABASES test")

for db in mycursor:
	print(db)

