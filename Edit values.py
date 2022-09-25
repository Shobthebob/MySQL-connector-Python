import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root" , password="" , database="")

mycursor = mydb.cursor( )
query = "UPDATE accounts SET <command> WHERE <command>"

mycursor.execute(query)
mydb.commit( )
