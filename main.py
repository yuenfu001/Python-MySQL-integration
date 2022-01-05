from mysql.connector import connection
import modules

print("CREATE A CONNECTION TO SQLWORKBENCH USING THIS PROGRAM")
hostname = input("Enter the hostname here: ") 
user_name=input("Enter Username here: ")
password = input("Enter password here: ")
connect = modules.create_server_conn(hostname, user_name, password)

while True:
    var = input("Enter 1: creating a database, 2: create table, 3: import csv to created database, 0: To exit : ")
    if var == "1":
        print("CREATE A DATABASE USING THIS PROGRAM")
        name = input("Enter your desired database name: ")
        modules.create_db(connect,name)
    elif var == "2":
        print("CREATE A TABLE OR INSERT VALUES INTO TABLE")
        name = input("Enter your name of database you want to connect to: ")
        table = input("Enter the SQL Query statement here: ")
        connection = modules.connect_server(hostname, user_name, password,name)
        modules.execute_query(connection, table)
        
    elif var == "3":
        print("IMPORT CSV INTO TABLE")
        df = input("Enter the csv file location to be imported: ")
        name = input("Enter your name of database you want to connect to: ")
        sql = input("Enter the SQL Query statement here: ")
        connection = modules.connect_server(hostname, user_name, password,name)
        modules.import_csv(connection, sql, df)
    elif var == "0":
        break
    else:
        print("{} isn't in the menu".format(var))
