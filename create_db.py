import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="admin", port="3308")

mycursor = mydb.cursor()
command = "CREATE DATABASE `python_db` COLLATE `utf8_bin`"

mycursor.execute(command)
print("Database Created")