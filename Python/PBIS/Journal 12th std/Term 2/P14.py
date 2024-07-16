import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='hArShAl_7',
    database='journal',
)

mycursor =mydb.cursor()

mycursor.execute('SELECT * FROM employee')

myresult=mycursor.fetchall()
print(myresult)
for x in myresult:
    print(x)
    
    
