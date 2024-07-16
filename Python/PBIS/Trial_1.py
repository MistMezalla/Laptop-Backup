import random
c=int(input('Enter(r): '))
r=[1,2,3,4,5,6]
while True:
    if c not in r:
        break
    n=random.randint(1,6)
    print(n)
