import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "admin", db = "python_db", port = "3308")

mycursor = mydb.cursor()

sql = "INSERT INTO `contact_list` (`id`, `name`, `phone`) VALUES (NULL, 'Test Name', '8013576138');"

mycursor.execute(sql)
print("Inserted")