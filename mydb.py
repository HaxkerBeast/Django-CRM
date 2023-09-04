import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Sanskar@12',
)

# prepare cursor object
cursorObject = dataBase.cursor()

# create dataBase
cursorObject.execute("CREATE DATABASE Animal_Rescue")

print("ALL DONE")