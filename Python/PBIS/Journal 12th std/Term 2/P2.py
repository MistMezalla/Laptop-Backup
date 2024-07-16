s=[]
c="y"
while (c=="y"):
    print ("1. PUSH")
    print ("2. POP ")
    print ("3. Display")
    choice=input("Enter your choice: ")
    if (choice==str(1)):
        a=input("Enter any number :")
        s.append(a)
    elif (choice==str(2)):
        if (s==[]):
            print ("Stack Empty")
        else:
            print ("Deleted element is : ",s.pop())
    elif (choice==str(3)):
        l=len(s)
        for i in range(l-1,-1,-1):
            print (s[i])
    else:
        print("Wrong Input")
    c=input("Do you want to continue or not? ")
