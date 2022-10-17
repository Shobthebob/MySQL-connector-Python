import mysql.connector

mydb = mysql.connector.connect(host="", user="" , password="" , database="")

mycursor = mydb.cursor( )
query = "DELETE FROM accounts WHERE <command>'"

mycursor.execute(query)
mydb.commit( )
