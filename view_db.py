import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="admin", port="3308")

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for db in mycursor:
    print(db)