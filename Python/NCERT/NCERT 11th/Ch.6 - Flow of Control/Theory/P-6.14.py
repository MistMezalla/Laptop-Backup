num1=int(input("Enter the number to be checked as prime or not: "))

flag=0 

if num1>1:
    for divisor in range(2,num1):
        if num1%divisor==0:
            flag=1  #This variable is given as this a link for our if condition validity. If this varaible wasn't there and only "Break" was given to the program then wriiten the print command then condtion of if statement holds no link to print statement.  
            break

    if flag==1:
        print(num1, "is composite")

    else:
        print(num1, "is prime number")

elif num1==1:
    print(num1, 'is neither prime nor composite')

elif num1<0:
    print('Wrong input, enter a postive number')
