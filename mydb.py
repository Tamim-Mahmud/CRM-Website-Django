import mysql.connector

database =mysql.connector.connect(
    host='localhost',
    user ='admin',
    passwd ='admin'
)

# [prepare a cursor object]  
# cursor is a database object that enables traversal of the result set of a query. A cursor provides a way to iterate over the rows returned by a SELECT statement. It allows you to process each row one at a time rather than fetching the entire result set into memory.

cursorObject =database.cursor()

# create a database 

cursorObject.execute("CREATE DATABASE crmdb")

print('DataBase Created !')

