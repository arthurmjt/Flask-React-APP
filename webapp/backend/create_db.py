"""
*** VERY IMPORTANT: Ony Run This File Once ***
To create database
"""
import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="ABCabc123!",
	)

my_cursor = mydb.cursor()

"""uncommand the line below when you run the file"""
# my_cursor.execute("CREATE DATABASE mag")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
	print(db)