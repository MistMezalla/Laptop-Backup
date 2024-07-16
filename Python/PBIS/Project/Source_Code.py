import mysql.connector

db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='hArShAl_7',
    database='project')

if db.is_connected()==False:
    print('connetion not established')
elif db.is_connected()==True:
    print('connection established')

mycursor=db.cursor()

def View_Product():
    c='y'
    while c.lower()=='y':
        mycursor.execute('select * from product')
        data=mycursor.fetchall()
        
        if data==[]:
            print('no data in this table ')
        else:
            for row in data:
                print(row)

        c=input("Do u want to continue, press 'y' to continue or any other key to exit ")
        
def Add_Product():
    c='y'
    while c.lower()=='y':
        Product_ID=input('Enter the id of the product: ' )
        Product_name=input('Enter the name of the product: ' )
        Rate=float(input('Enter the rate of the product: ' ))
        Status=input('Enter the status of the product:- Availabele or Unavailable ')
        
        ins="insert into product(Product_ID,Product_name,Rate,Status) values('{}','{}',{},'{}')".format(Product_ID,Product_name,Rate,Status)
        mycursor.execute(ins)
        db.commit()

        print('Data corresponding to',Product_name,'with Product_ID',Product_ID,'is added')

        c=input("Do u want to continue, press 'y' to continue or any other key to exit ")


def Update_Product():
    c='y'
    while c.lower()=='y':
        pid=input('Enter the Product_ID of the product to be updated: ')
        feild=input('Enter the field to be updated: ')
        new_value=input('Enter the new value to be updated: ')

        update="update product set {}='{}' where Product_ID=('{}')".format(feild,new_value,pid)
        mycursor.execute(update)
        db.commit()

        print(feild,'of',pid,'is updated to',new_value)
        c=input("Do u want to continue, press 'y' to continue or any other key to exit ")

def View_Purchase():
    c='y'
    while c.lower()=='y':
        mycursor.execute('select * from purchase')
        data=mycursor.fetchall()
        
        if data==[]:
            print('no data in this table ')
        else:
            for row in data:
                print(row)

        c=input("Do u want to continue, press 'y' to continue or any other key to exit ")

def Add_Purchase():
    c='y'
    while c.lower()=='y':
        Purchase_ID=input('Enter the id of the purchase: ' )
        item_ID=input('Enter the id of the item: ' )
        item_name=input('Enter the name of the item: ' )
        no_of_items=int(input('Enter the no of items: '))
        Rate=float(input('Enter the rate of the product: ' ))
        Amount=no_of_items*Rate
        Purchase_date=input("Enter the date of purchase in format 'YYYY-MM-DD': ")
        
        ins="insert into purchase(Purchase_ID,item_ID,item_name,no_of_items,Rate,Amount,Purchase_date) values('{}','{}','{}',{},{},{},'{}')".format(Purchase_ID,item_ID,item_name,no_of_items,Rate,Amount,Purchase_date)
        mycursor.execute(ins)
        db.commit()

        st="insert into stock(item_ID) values('{}')".format(item_ID)
        mycursor.execute(st)

        db.commit()
        
        st1="select * from stock where item_ID = '{}'".format(item_ID)
        mycursor.execute(st1)

        data=mycursor.fetchall()
        

        Sitem=data[0][3]
        Sitem+=no_of_items

        upitem="update stock set no_of_items = {} where item_ID=('{}')".format(Sitem,item_ID)
        mycursor.execute(upitem)
        db.commit()
        

        print('Data corresponding to',item_name,'with item_ID',item_ID,'is added')

        c=input("Do u want to continue, press 'y' to continue or any other key to exit ")



def Update_Purchase():
    c='y'
    while c.lower()=='y':
        iid=input('Enter the item_ID of the item to be updated: ')
        feild=input('Enter the field to be updated: ')
        new_value=input('Enter the new value to be updated: ')

        if feild=='no_of_items':
            st="select * from purchase where item_ID = '{}'".format(iid)
            mycursor.execute(st)

            data=mycursor.fetchall()
            
            rate=data[0][4]
            amount=int(new_value)*rate
            
            update="update purchase set {}='{}' where item_ID=('{}')".format(feild,new_value,iid)
            mycursor.execute(update)

            db.commit()

            upamt="update purchase set Amount = {} where item_ID=('{}')".format(amount,iid)
            mycursor.execute(upamt)

            db.commit()
            
            st1="select * from stock where item_ID = '{}'".format(iid)
            mycursor.execute(st1)

            data=mycursor.fetchall()
            
            Sitem=data[0][3]
            old_value=int(input('Enter the old value to be updated: '))
            Sitem-=old_value
            Sitem+= int(new_value)

            upitem="update stock set no_of_items = {} where item_ID=('{}')".format(Sitem,iid)
            mycursor.execute(upitem)
            db.commit()
        
            print(feild,'of',iid,'is updated to',new_value)

        elif feild=='Rate':
            st="select * from purchase where item_ID = '{}'".format(iid)
            mycursor.execute(st)

            data=mycursor.fetchall()
            
            no_of_items=data[0][3]
            amount=int(new_value)*no_of_items

            update="update purchase set {}='{}' where item_ID=('{}')".format(feild,new_value,iid)
            mycursor.execute(update)

            db.commit()

            upamt="update purchase set Amount = {} where item_ID=('{}')".format(amount,iid)
            mycursor.execute(upamt)

            db.commit()
            print(feild,'of',iid,'is updated to',new_value)

        else:
            update="update purchase set {}='{}' where item_ID=('{}')".format(feild,new_value,iid)
            mycursor.execute(update)

            db.commit()
            print(feild,'of',iid,'is updated to',new_value)

        c=input("Do u want to continue, press 'y' to continue or any other key to exit ")

def View_Stock():
    c='y'
    while c.lower()=='y':
        mycursor.execute('select * from stock')
        data=mycursor.fetchall()
        
        if data==[]:
            print('no data in this table ')
        else:
            for row in data:
                print(row)

        c=input("Do u want to continue, press 'y' to continue or any other key to exit ")


def View_Sale():
    c='y'
    while c.lower()=='y':
        mycursor.execute('select * from sale')
        data=mycursor.fetchall()
        
        if data==[]:
            print('no data in this table ')
        else:
            for row in data:
                print(row)

        c=input("Do u want to continue, press 'y' to continue or any other key to exit ")

def Add_Sale():
    c='y'
    while c.lower()=='y':
        Sale_ID=input('Enter the id of the sale: ' )
        Product_ID=input('Enter the id of the product: ' )
        Product_name=input('Enter the name of the product: ' )
        no_of_products_sold=int(input('Enter the no of product sold: '))
        Rate=float(input('Enter the rate of the product: ' ))
        Amount=no_of_products_sold*Rate
        Sale_date=input("Enter the date of sale in format 'YYYY-MM-DD': ")
        
        ins="insert into sale(Sale_ID,Product_ID,Product_name,no_of_products_sold,Rate,Amount,Sale_date) values('{}','{}','{}',{},{},{},'{}')".format(Sale_ID,Product_ID,Product_name,no_of_products_sold,Rate,Amount,Sale_date)
        mycursor.execute(ins)
        db.commit()

        st1="select * from stock where Product_ID = '{}'".format(Product_ID)
        mycursor.execute(st1)

        data=mycursor.fetchall()
        Sproduct=data[0][2]
        Sproduct-=no_of_products_sold

        upproduct="update stock set no_of_products = {} where Product_ID=('{}')".format(Sproduct,Product_ID)
        mycursor.execute(upproduct)
        db.commit()
        

        print('Data corresponding to',Product_name,'with item_ID',Product_ID,'is added')

        c=input("Do u want to continue, press 'y' to continue or any other key to exit ")

def Update_Sale():
    c='y'
    while c.lower()=='y':
        pid=input('Enter the Product_ID of the item to be updated: ')
        feild=input('Enter the field to be updated: ')
        new_value=input('Enter the new value to be updated: ')

        if feild=='no_of_products_sold':
            st="select * from sale where Product_ID = '{}'".format(pid)
            mycursor.execute(st)

            data=mycursor.fetchall()
            
            rate=data[0][4]
            amount=int(new_value)*rate
            
            update="update sale set {}='{}' where Product_ID=('{}')".format(feild,new_value,pid)
            mycursor.execute(update)

            db.commit()

            upamt="update sale set Amount = {} where Product_ID=('{}')".format(amount,pid)
            mycursor.execute(upamt)

            db.commit()
            
            st1="select * from stock where Product_ID = '{}'".format(pid)
            mycursor.execute(st1)

            data=mycursor.fetchall()
            
            Sproduct=data[0][2]
            old_value=int(input('Enter the old value to be updated: '))
            Sproduct+=old_value
            Sproduct-= int(new_value)

            upproduct="update stock set no_of_products = {} where Product_ID=('{}')".format(Sproduct,pid)
            mycursor.execute(upproduct)
            db.commit()
        
            print(feild,'of',pid,'is updated to',new_value)

        elif feild=='Rate':
            st="select * from sale where Product_ID = '{}'".format(pid)
            mycursor.execute(st)

            data=mycursor.fetchall()
            
            no_of_products_sold=data[0][3]
            amount=int(new_value)*no_of_products_sold

            update="update sale set {}='{}' where Product_ID=('{}')".format(feild,new_value,pid)
            mycursor.execute(update)

            db.commit()

            upamt="update sale set Amount = {} where Product_ID=('{}')".format(amount,pid)
            mycursor.execute(upamt)

            db.commit()
            print(feild,'of',pid,'is updated to',new_value)

        else:
            update="update sale set {}='{}' where Product_ID=('{}')".format(feild,new_value,pid)
            mycursor.execute(update)

            db.commit()
            print(feild,'of',pid,'is updated to',new_value)

        c=input("Do u want to continue, press 'y' to continue or any other key to exit ")



def View_Processing():
    c='y'
    while c.lower()=='y':
        mycursor.execute('select * from processing')
        data=mycursor.fetchall()
        
        if data==[]:
            print('no data in this table ')
        else:
            for row in data:
                print(row)

        c=input("Do u want to continue, press 'y' to continue or any other key to exit ")

def Add_Processing():
    c='y'
    while c.lower()=='y':
        print('Choose what u want to add.\n1.Item\n2.Product')
        choice=int(input('Enter your choice: '))

        if choice==1:
            item_ID=input('Enter the id of the item: ')
            no_of_items_processed=int(input('Enter the number of items processed: '))
                
            ins="insert into processing(item_ID,no_of_items_processed) values('{}',{});".format(item_ID,no_of_items_processed)
            print(ins)
            mycursor.execute(ins)
            db.commit()
            
            '''
            st="insert into stock(item_ID) values('{}')".format(item_ID)
            mycursor.execute(st)

            db.commit()
            '''
            st1="select * from stock where item_ID = '{}'".format(item_ID)
            mycursor.execute(st1)

            data=mycursor.fetchall()
            
            Sitem=data[0][3]
            Sitem-=no_of_items_processed

            upitm="update stock set no_of_items = {} where item_ID=('{}')".format(Sitem,item_ID)
            mycursor.execute(upitm)
            db.commit()
            print('Data corresponding to',item_ID,'is added')
            
        elif choice==2:
            Product_ID=input('Enter the id of the product: ')
            no_of_product_made=int(input('Enter the number of products made: '))
                
            ins="insert into processing(Product_ID,no_of_product_made) values('{}',{})".format(Product_ID,no_of_product_made)
            mycursor.execute(ins)
            db.commit()

            st="insert into stock(Product_ID) values('{}')".format(Product_ID)
            mycursor.execute(st)

            db.commit()
            st1="select * from stock where Product_ID = '{}'".format(Product_ID)
            mycursor.execute(st1)

            data=mycursor.fetchall()
            
            Sproduct=data[0][2]
            Sproduct+=no_of_product_made
            upproduct="update stock set no_of_products = {} where Product_ID=('{}')".format(Sproduct,Product_ID)
            mycursor.execute(upproduct)
            db.commit()
                
            print('Data corresponding to',Product_ID,'is added')

        c=input("Do u want to continue, press 'y' to continue or any other key to exit ")

def Update_Processing():
    c='y'
    while c.lower()=='y':
        print('Choose what u want to update.\n1.Item\n2.Product')
        choice=int(input('Enter your choice: '))

        if choice==2:
            pid=input('Enter the Product_ID of the product to be updated: ')
            feild=input('Enter the field to be updated: ')
            new_value=input('Enter the new value to be updated: ')

            if feild=='no_of_product_made':
                update="update processing set {}='{}' where Product_ID=('{}')".format(feild,new_value,pid)
                mycursor.execute(update)

                db.commit()
                
                st1="select * from stock where Product_ID = '{}'".format(pid)
                mycursor.execute(st1)

                data=mycursor.fetchall()
                
                Sproduct=data[0][2]
                old_value=int(input('Enter the old value to be updated: '))
                Sproduct-=old_value
                Sproduct+= int(new_value)

                upproduct="update stock set no_of_products = {} where Product_ID=('{}')".format(Sproduct,pid)
                mycursor.execute(upproduct)
                db.commit()
            
                print(feild,'of',pid,'is updated to',new_value)

            else:
                update="update processing set {}='{}' where Product_ID=('{}')".format(feild,new_value,pid)
                mycursor.execute(update)

                db.commit()
                print(feild,'of',pid,'is updated to',new_value)

            c=input("Do u want to continue, press 'y' to continue or any other key to exit ")

        if choice==1:
            iid=input('Enter the item_ID of the item to be updated: ')
            feild=input('Enter the field to be updated: ')
            new_value=input('Enter the new value to be updated: ')

            if feild=='no_of_items_processed':
                update="update processing set {}='{}' where item_ID=('{}')".format(feild,new_value,iid)
                mycursor.execute(update)

                db.commit()
                
                st1="select * from stock where item_ID = '{}'".format(iid)
                mycursor.execute(st1)

                data=mycursor.fetchall()
                
                Sitem=data[0][3]
                old_value=int(input('Enter the old value to be updated: '))
                Sitem+=old_value
                Sitem-= int(new_value)

                upitem="update stock set no_of_items = {} where item_ID=('{}')".format(Sitem,iid)
                mycursor.execute(upitem)
                db.commit()
            
                print(feild,'of',iid,'is updated to',new_value)

            else:
                update="update processing set {}='{}' where item_ID=('{}')".format(feild,new_value,iid)
                mycursor.execute(update)

                db.commit()
                print(feild,'of',iid,'is updated to',new_value)

            c=input("Do u want to continue, press 'y' to continue or any other key to exit ")
            
while True:
    print('WELCOME TO NOVEL COOKWARE Pvt. Ltd.')
    print('MAIN MENU\nEnter the corresponding number to perform the functions on tables given below')
    print('1 = Product\n2 = Purchase\n3 = Processing\n4 = Sale\n5 = Stock\n6 = To exit the inventory')
    choice=int(input('Enter your choice: '))

    if choice==1:
        p='y'
        while p.lower()=='y':
            print('PRODUCT TABLE\nEnter the corresponding number to perform the functions listed below')
            print('1 = View table\n2 = Add data to table\n3 = Update data in table')
            choice_p=int(input('Enter your choice: '))

            if choice_p==1:
                View_Product()
            elif choice_p==2:
                Add_Product()
            elif choice_p==3:
                Update_Product()
            else:
                print('Wrong input')

            p=input("Do you want to continue?\nPress 'y' to continue or 'm' to return to main menu: ")

    if choice==2:
        p='y'
        while p.lower()=='y':
            print('PURCHASE TABLE\nEnter the corresponding number to perform the functions listed below')
            print('1 = View table\n2 = Add data to table\n3 = Update data in table')
            choice_p=int(input('Enter your choice: '))

            if choice_p==1:
                View_Purchase()
            elif choice_p==2:
                Add_Purchase()
            elif choice_p==3:
                Update_Purchase()
            else:
                print('Wrong input')

            p=input("Do you want to continue?\nPress 'y' to continue or 'm' to return to main menu: ")

    if choice==3:
        p='y'
        while p.lower()=='y':
            print('PROCESSING TABLE\nEnter the corresponding number to perform the functions listed below')
            print('1 = View table\n2 = Add data to table\n3 = Update data in table')
            choice_p=int(input('Enter your choice: '))

            if choice_p==1:
                View_Processing()
            elif choice_p==2:
                Add_Processing()
            elif choice_p==3:
                Update_Processing()
            else:
                print('Wrong input')

            p=input("Do you want to continue?\nPress 'y' to continue or 'm' to return to main menu: ")

    if choice==4:
        p='y'
        while p.lower()=='y':
            print('SALE TABLE\nEnter the corresponding number to perform the functions listed below')
            print('1 = View table\n2 = Add data to table\n3 = Update data in table')
            choice_p=int(input('Enter your choice: '))

            if choice_p==1:
                View_Sale()
            elif choice_p==2:
                Add_Sale()
            elif choice_p==3:
                Update_Sale()
            else:
                print('Wrong input')

            p=input("Do you want to continue?\nPress 'y' to continue or 'm' to return to main menu: ")

    if choice==5:
        p='y'
        while p.lower()=='y':
            print('STOCK TABLE\nEnter the corresponding number to perform the functions listed below')
            print('1 = View table')
            choice_p=int(input('Enter your choice: '))

            if choice_p==1:
                View_Stock()
            else:
                print('Wrong input')

            p=input("Do you want to continue?\nPress 'y' to continue or 'm' to return to main menu: ")

    if choice==6:
        break



            












    


        

    
    


    
    

