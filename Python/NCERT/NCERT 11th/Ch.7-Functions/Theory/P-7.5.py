def value_incr(n):
    print(id(n))
    n+=5
    print(n)
    print(id(n))

num=int(input('Enter the number: '))
print(id(num))

value_incr(num)
