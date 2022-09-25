import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root" , password="" , database="")

mycursor = mydb.cursor( )
query = "DELETE FROM accounts WHERE <command>'"

mycursor.execute(query)
mydb.commit( )
