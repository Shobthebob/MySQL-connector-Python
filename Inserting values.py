import mysql.connector

mydb = mysql.connector.connect(host="", user="" , password="" , database="")

mycursor = mydb.cursor( )
query = "INSERT INTO <table> values(%s,%s)"

user = input("Enter a username: ")
pas = input("Enter a passcode: ")
acc = [(user,pas)]

mycursor.executemany(query, acc)

mydb.commit( )
