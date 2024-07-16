def menu():
    c='y'
    while c=='y':
        print('1.Add record')
        print('2.Update record')
        print('3.Delete record')
        print('4.Display record')
        print('5.Exiting')

        choice=int(input('Enter your choice: '))

        if choice==1:
            adddata()
        elif choice==2:
            updatedata()
        elif choice==3:
            deldata()
        elif choice==4:
            fetchdata()
        elif choice==5:
            print('Exiting')
            break
        else:
            print('wrong input')

        c=input("do you want to continue or not: ")

def fetchdata():
    import mysql.connector

    try:
        db=mysql.connector.connect(
            host='localhost',
            user='root',
            password='hArShAl_7',
            database='s1')

        cursor=db.cursor()
        cursor.execute('select * from student')
        results=cursor.fetchall()

        if results==[]:
            print('no data in table')
        else:
            for x in results:
                print(x)

    except:
        print('Error: unable to fetch data')

def adddata():
    import mysql.connector
    db=mysql.connector.connect(
            host='localhost',
            user='root',
            password='hArShAl_7',
            database='s1')

    cursor=db.cursor()
    cursor.execute("insert into student values('Ritu',4000,'Science',345,'B','11')")
    cursor.execute("insert into student values('Ankush',6000,'Commerce',445,'A','12')")
    cursor.execute("insert into student values('Pihu',3000,'Humanity',446,'A','11')")
    cursor.execute("insert into student values('Tinku',8900,'Science',345,'A+','12')")

    db.commit()
    print('record added')

def updatedata():
    import mysql.connector

    try:
        db=mysql.connector.connect(
            host='localhost',
            user='root',
            password='hArShAl_7',
            database='s1')

        cursor=db.cursor()
        cursor.execute("update student set stipend=5000 where name='Ritu'")

        print('record updated')
        db.commit()

    except Exception as e:
        print(e)

def deldata():
     import mysql.connector
     db=mysql.connector.connect(
            host='localhost',
            user='root',
            password='hArShAl_7',
            database='s1')

     cursor=db.cursor()
     cursor.execute("delete from student where name='Ritu'")

     print('record deleted')
     db.commit()

menu()

    
    
    
    
