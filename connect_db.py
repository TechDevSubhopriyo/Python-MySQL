import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="admin", port="3308")

if(mydb):
    print("Connection Successful")
else:
    print("Connection Failed")