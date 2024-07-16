def Delete_Product():
    c='y'
    while c.lower()=='y':
        pid=input('Enter the Product_ID of the product to be deleted: ')

        delete="delete from product where Product_ID={}".format(pid)
        mycursor.execute(delete)
        db.commit()

        print('Data corresponding to',pid,'is deleted')
        c=input("Do u want to continue, press 'y' to continue or any other key to exit ")

def Delete_Purchase():
    c='y'
    while c.lower()=='y':
        iid=input('Enter the item_ID of the item to be deleted: ')

        delete="delete from purchase where item_ID='{}'".format(iid)
        mycursor.execute(delete)
        db.commit()

        delete="delete from stock where item_ID='{}'".format(iid)
        mycursor.execute(delete)
        db.commit()

        print('Data corresponding to',iid,'is deleted')
        c=input("Do u want to continue, press 'y' to continue or any other key to exit ")
def Delete_Sale():
    c='y'
    while c.lower()=='y':
        pid=input('Enter the Product_ID of the product to be deleted: ')

        delete="delete from sale where Product_ID='{}'".format(pid)
        mycursor.execute(delete)
        db.commit()

        delete="delete from stock where Product_ID='{}'".format(pid)
        mycursor.execute(delete)
        db.commit()

        print('Data corresponding to',pid,'is deleted')
        c=input("Do u want to continue, press 'y' to continue or any other key to exit ")

        
