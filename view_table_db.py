import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="admin", database="python_db", port="3308")

mycursor = mydb.cursor()

tables = mycursor.execute("Show tables")

if(tables != None):
    for table in tables:
        print(table)