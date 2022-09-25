import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root" , password="shob25" , database="test")

mycursor = mydb.cursor( )
mycursor.execute("Select username from accounts")

myresult = mycursor.fetchall( )

un = "u1"

for row in myresult:
	print(row)