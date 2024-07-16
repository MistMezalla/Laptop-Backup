num1=int(input("Enter the number whose factors are to be found: "))

print(1)

factor=2

while factor <= num1 :
    if num1%factor==0 :
        print(factor)
        factor+=1
        
    else:
         factor+=1

'''
If the else statement is not written then for factors which dont give%==0
the the while loop will terminate due to fallacy of the if satement.
'''
