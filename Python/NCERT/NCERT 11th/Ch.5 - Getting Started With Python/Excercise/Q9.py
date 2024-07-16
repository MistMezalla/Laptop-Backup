#Q9
# Eqn of circle : x**2+y**2=100

t=0
while t==0:
    x=float(input('Enter the x cooordinate: '))
    y=float(input('Enter the y cooordinate: '))

    if x**2+y**2 <= 100:
        print('hit')
    else:
        print('miss')
    t=int(input('Do u want to continue, 0 or 1: '))
