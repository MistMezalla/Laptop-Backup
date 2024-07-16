import random
while(True):
    c=input('Enter (r) for roll dice or press any key to quit')
    if(c!=''):
        break
n=random.randint(1,6)
print(n)

