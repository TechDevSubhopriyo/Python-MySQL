import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="admin", database="python_db", port="3308")

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE `contact_list`(id int AUTO_INCREMENT, name varchar(50), phone int(15), PRIMARY KEY (id)) COLLATE 'utf8_bin'")
if(mycursor._executed):
    print("Table created")