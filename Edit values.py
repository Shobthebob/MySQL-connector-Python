import mysql.connector

mydb = mysql.connector.connect(host="", user="" , password="" , database="")

mycursor = mydb.cursor( )
query = "UPDATE accounts SET <command> WHERE <command>"

mycursor.execute(query)
mydb.commit( )
