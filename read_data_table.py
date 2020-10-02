import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="admin", database="python_db", port="3308")

mycursor = mydb.cursor()
sql = "Select * From `contact_list`"
mycursor.execute(sql)

rows = mycursor.fetchall()

for row in rows:
    print(row)