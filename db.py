import mysql.connector
def connect():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sruthip0222@",
        database="Practice_crt"
    )
    return conn
if(connect()):
    print("Connection established successfully")
else:
    print("Connection failed")