import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root" , password="" , database="")

mycursor = mydb.cursor( )
mycursor.execute("Select <column> from <db>")

myresult = mycursor.fetchall( )

for row in myresult:
	print(row)
