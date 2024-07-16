for num in range (2,51):
    for divisor in range(2,num): #due to 51 instead of num the loop was getting executed over 2000 times and for every number the constraint laid should be that divisor should be less than num and not 51.
        if num%divisor==0: 
                break
    else:
        print(num)
