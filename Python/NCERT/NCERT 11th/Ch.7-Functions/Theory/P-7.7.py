def calcFact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)

num=int(input('Enter the number whose factorial is to be found: '))

calcFact(num)
