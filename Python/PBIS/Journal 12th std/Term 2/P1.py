# without classes
a=[]
c='y'
while c=='y':
    print('1.INSERT')
    print('2.DELETE')
    print('3.Display')
    choice=input('enter your choice ')
    if(choice==str(1)):
        b=input('enter new number ')
        a.append(b)
    elif(choice==str(2)):
        if(a==[]):
            print('Queue Empty')
        else:
            print('deleted element is:',a[0])
            del a[0]
    elif(choice==str(3)):
        l=len(a)
        for i in range(0,1):
            print(a[i])
    else:
        print('wrong input')
    c=input('do you want to continue or not ')

#with classes
class queue:
    q=[]
    def insertion(self):
        self=input('enter any nnumber ')
        queue.q.append(self)
    def deletion(self):
        if(queue.q==[]):
            print('Queue empty')
        else:
            print("deleted element is: ",queue.q[0])
            del queue.q[0]
    def display(self):
        l=len(queue.q)
        for i in range(0,l):
            print (queue.q[i])

    def __init__ (self):
        c="y"
        while (c=="y"):
            print ("1. INSERTION")
            print ("2. DELETION ")
            print ("3. DISPLAY")
            choice=input("enter your choice: ")
            if (choice==str(1)):
                self.insertion()
            elif (choice==str(2)):
                self.deletion()
            elif (choice==str(3)):
                self.display()
            else:
                print("wrong input")
            c=input("do you want to continue or not :")

a=queue()
            
