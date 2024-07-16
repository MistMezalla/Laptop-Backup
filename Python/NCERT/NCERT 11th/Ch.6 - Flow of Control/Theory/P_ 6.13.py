num1=0
sum1=0

# If here num1=int(input("Enter the number to be summed: ")) was there then first input won't be the part of the while loop.

while True :

    # If 'if' statement was been used as num1>=0 then the -ve number is shown as result and there leads to error in as the 1st element is not considered in the sum and the -ve number is also added to the sum.
    num1=int(input("Enter the number to be summed: "))
          
    if num1<0 :
        break
    else:
        sum1+=num1
print(sum1)

    
    

    
        
        
    
    
    
