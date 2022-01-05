import mysql.connector as mysql
from mysql.connector import Error
import pandas as pd

# CREATE A SERVER CONNECTION BETWEEN PYTHON AND MYSQL SERVER CRTL+/ = commenting 
def create_server_conn(hostname, user_name, password):
    connection = None
    try:
        connection = mysql.connect(
            host = hostname,
            user = user_name,
            passwd = password
        )
        print("MySQL server connection has been establised successfully")
    
    except Error as err:
        print(f" Error: {err}")
    return connection

def connect_server(hostname, user_name,password, database):
    connection = None
    try:
        connection = mysql.connect(
            host = hostname,
            user = user_name,
            passwd = password,
            database = database
        )
        print("MySQL Database connection has been establised successfully")
    
    except Error as err:
        print(f" Error: {err}")
    return connection

def create_db(connection, name):
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE {}".format(name))
        
        print("Database created successfully")
    
    except Error as err:
        print(f"Error: {err}")


#"CREATE DATABASE cleanDBs"

def execute_query(connection, query):
    
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    
    except Error as err:
        print(f" Error: {err}")

def import_csv(connection, sql, df):
    cursor = connection.cursor()
    # sql = "INSERT INTO taskdb (DateTime,NOx,NO2,NO,SiteID,PM10,NVPM10,VPM10,NVPM2,PM2,VPM2,CO,O3,SO2,Temperature,RH,AirPressure,Location,geo_point_2d,DateStart,DateEnd,Current,InstrumentType) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    print("Importing csv")
    for i in df:
        print(i)
        cursor.execute(sql,i)
    connection.commit()
    cursor.close()
    print("Done")