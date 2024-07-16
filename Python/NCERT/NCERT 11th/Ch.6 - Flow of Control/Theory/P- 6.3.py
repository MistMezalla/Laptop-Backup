op=input("Enter any one of the following operator (+,-,*,/): ")
num1=float(input("Enter the 1st number: "))
num2=float(input("Enter the 2nd number: "))

if op=='+' :
         print(num1+num2)

elif op=='-' :
    if num1>num2 :
        print=(num1-num2)
    elif num1<num2 :
        print=(num2-num1)

elif op=='*' :
    print(num1*num2)

elif op=='/' :
    if num2 ==0 :
        print("Enter number other than 0")
    else :
        print(num1/num2)

else :
    print('wrong input')

    

