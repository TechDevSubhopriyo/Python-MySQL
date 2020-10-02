import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="admin", database="python_db", port="3308")

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for table in mycursor:
    print(table)