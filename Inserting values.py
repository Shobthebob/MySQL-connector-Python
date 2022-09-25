import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root" , password="shob25" , database="test")

mycursor = mydb.cursor( )
sqlform = "INSERT INTO accounts values(%s,%s)"

user = input("Enter a username: ")
pas = input("Enter a passcode: ")
acc = [(user,pas)]

mycursor.executemany(sqlform, acc)

mydb.commit( )
