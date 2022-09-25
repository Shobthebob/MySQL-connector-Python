import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root" , password="shob25" , database="test")

mycursor = mydb.cursor( )
sql = "DELETE FROM accounts WHERE Username='Shobthebob'"

mycursor.execute(sql)
mydb.commit( )