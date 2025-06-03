'''
use practice_crt;
create table Student (
     roll_no int primary key,
     name varchar(20) not null,
     branch varchar(50) not null
);
'''
from db import connect
conn=connect()
if conn:
    print("Connection established successfully")
else:
    print("Connection failed")
def Insert_data():
    roll_no=int(input("Enter roll number: "))
    name=input("Enter name: ")
    branch=input("Enter branch: ")
    cursor=conn.cursor()
    query="insert into Student values(%s,%s,%s)" #%s-this is a phase holder where it holds the values
    values=(roll_no,name,branch)
    cursor.execute(query,values)
    conn.commit()
    print("Data inserted successfully") 
def fetch_data():
   cursor=conn.cursor()
   query="Select * from Student"
   cursor.execute(query)
   results=cursor.fetchall()
   for row in results:
       print(row)
# fetch_data()#Function call
def update_data():
    roll_no=int(input("Enter roll number to update: "))
    name=input("Enter new name: ")
    branch=input("Enter new branch: ")
    cursor=conn.cursor()
    query="update Student set name=%s,branch=%s where roll_no=%s" #%s-this is a phase holder where it holds the values
    values=(name,branch,roll_no)
    cursor.execute(query,values)
    conn.commit()
    print("Data updated successfully") 
#While loop to perform operations
print("1. Insert data")
print("2. fetch data")
print("3. update data")
print("4. Exit")
while True:
    choice=int(input("Enter yor choice: "))
    if choice==1:
        Insert_data()
    elif choice==2:
        fetch_data()
    elif choice==3:
        update_data()
    elif choice==4:
        print("exit")
        break

