import mysql.connector

# Establish connection
connection = mysql.connector.connect(
        host= 'localhost',
        user= 'root',
        passwd= 'habakkuk10tamunosakijacob',
        database='eventifycollins'
        )

cursor = connection.cursor()

cursor.execute('SHOW TABLES')

tables = cursor.fetchall()
for table in tables:
    print(table[0])

    
cursor.close()
connection.close()