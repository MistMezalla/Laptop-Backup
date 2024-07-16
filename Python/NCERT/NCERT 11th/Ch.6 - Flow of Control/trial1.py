for num in range (2,51):
    for divisor in range(2,51):
        if num%divisor==0:
            break
    else:
        print(num)
