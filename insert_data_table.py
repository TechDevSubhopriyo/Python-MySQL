import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "admin", db = "python_db", port = "3308")

mycursor = mydb.cursor()
name=input("Enter Name:- ")
phone=input("Enter phone:- ")


sql = "INSERT INTO `contact_list` (`id`, `name`, `phone`) VALUES (NULL, '"+name+"', '"+phone+"');"

mycursor.execute(sql)
print("Inserted")