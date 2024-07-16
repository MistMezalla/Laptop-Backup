#Solved Programs
def P_9_3():
    n=int(input('Number of numbers?: '))
    l=[]
    for i in range(0,n):
        x=float(input('Enter the number:'))
        l.append(x)
    s=set(l)
    sm1=sum(l)
    sm2=sum(s)
    print(sm1,sm2)

def P_9_5():
    n=int(input('Number of numbers?: '))
    l=[];d=[]
    for i in range(0,n):
        x=float(input('Enter the number:'))
        l.append(x)
    num=float(input('Enter the number to be tested: '))

    for i in l:
        if num%i==0:
            d.append(i)
    print('Div numbers are: ',d)
            
def P_9_9():
    ch=input('Enter the value: ')

    if len(ch)==1:
        if ch>='A' and ch<='Z':
            print('Uppercase')
        elif ch>='a' and ch<='z':
            print('Lowercase')
        elif ch>='0' and ch<='9':
            print('Digit')
        else:
            print('Sp Char')
    else:
        print('Others')

def P_9_10():
    a=float(input('Enter the value of a: '))
    b=float(input('Enter the value of b: '))
    c=float(input('Enter the value of c: '))

    dis=b**2-(4*a*c)
    from math import sqrt
    
    if a!=0 and dis>=0:
        x=(-b+sqrt(dis))/(2*a)
        y=(-b-sqrt(dis))/(2*a)
        print(x,'or',y)
    elif a==0:
        x=-c/b
        print(x)
    elif dis<0:
        print('No solution')

    

r=0
while r==0:
    P_9_10()
    r=int(input())
    
