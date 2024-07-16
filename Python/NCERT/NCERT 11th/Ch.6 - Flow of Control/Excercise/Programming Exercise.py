#Programming Exercise
def P_1():
    name=input('Enter your name: ')
    age=int(input('Enter your age: '))

    if age>=18:
        print('Eligible')
    elif age<18 and age>0:
        print('Ineligible')
    else:
        print('Plz enter your age in positve integer')

def P_2():
    num=int(input('Enter the number: '))

    for i in range (1,11):
        print(num*i)

def P_3():
    l=[]
    for i in range (0,5):
        num=float(input('Enter the number: '))
        l.append(num)

    print(max(l),min(l))

def P_4():
    yr=int(input('Enter the year: '))
    if yr>=0:
        if yr%100==0:
            if yr%400==0:
                print('Leap Year')
            else:
                print('Non Leap Yr')
    
        else:
            if yr%4==0:
                print('Leap Year')
            else:
                print('Non Leap Yr')

    else:
        print('Enter a +ve int')

def P_5():
    n=int(input('Enter the number: '))
    for i in range (1,n+1):
        if i%2==0:
            print(10*int(i/2),end=' ')
        else:
            print(-5*i,end=' ')
    
def P_6():
    n=int(input('Enter the number: '))
    sm=0
    for i in range (1,n+1):
        sm+=1/(i**3)
    print(sm)
        
def P_7():
    n=int(input('Enter the number: '))
    sm=0
    for i in str(n):
        sm+=int(i)
    print(sm)   

def P_8():
    n=int(input('Enter the number: '))
    t=len(str(n))

    from math import ceil
    for i in range (0,ceil(t/2)):
        if (str(n)[i])==(str(n)[t-i-1]):
            m=1
        else:
            m=2
            break

    if m==1:
        print('Palindrome')
    else:
        print('Not palindrome')
        


def P_9_1_SA():
    n=5
    k=round(n/2)*2
    for i in range (0,n,2):
        for j in range (0,k+1):
            print(end=' ')
        for j in range (0,i+1):
            print('*',end='')
        k-=2
        print()

    k=1
    for i in range (n-1,0,2):
        for j in range (0,k+2):
            print(end=' ')
        for j in range (0,i-1):
            print('*',end='')
        k+=2
        print()
                
def P_9_1():
    #Upper Half
    k=2;l=1;m=2
    for i in range(0,3):
        for j in range (0,k):
            print(end='$')
        "print()"
        k-=1

        for x in range (0,l):
            print('*',end='')
        "print()"
        l+=2

        for j in range (0,m):
            print(end='&')
        print()
        m-=1

    #Lower Half
    a=1;b=3;c=1
    for t in range (0,2):
        for j in range (0,a):
            print(end='$')
        a+=1

        for j in range (0,b):
            print('*',end='')
        "print()"
        b-=2

        for j in range (0,c):
            print(end='&')
        print()
        c+=1

def P_9_2():
    a=4;b=2;c=4
    for i in range(0,5):
        for j in range (0,a):
            print(end='!')
        a-=1
        for j in range (i+1,0,-1):
            print(j,end='')
        
        for j in range (1,i+1):
            print(j+1,end='')
        b+=1
      
        for j in range (0,c):
            print(end='@')
        c-=1
        
        print()
        
def P_9_3():
    for i in range (5,0,-1):
        for j in range (0,5-i):
            print(end='#')
        for j in range (1,i+1):
            print(j,end='')
        print()

def P_9_4_1():
    for i in range (1,6):
        if i==1 or i==5:
            print(' '*2+'*'+' '*2)
        elif i==2 or i==4:
            print(' '+'*'+' '+'*'+' ')
        else:
            print('*'+' '*3+'*')

def P_9_4_2():
    n=int(input('Enter the number of line: '))

    if n%2!=0:
        m=int((n+1)/2)
        print(' '*(m-1)+'*'+' '*(m-1))

        for i in range (1,m):
            print(' '*(m-i-1)+'*'+' '*(2*i-1)+'*'+' '*(m-i-1))

        for i in range (m-2,0,-1):
            print(' '*(m-i-1)+'*'+' '*(2*i-1)+'*'+' '*(m-i-1))

        print(' '*(m-1)+'*'+' '*(m-1))

    else:
        m=int(n/2)
        print(' '*(m-1)+'*'+' '*(m-1))

        for i in range (1,m):
            print(' '*(m-i-1)+'*'+' '*(2*i-1)+'*'+' '*(m-i-1))

        for i in range (m-1,0,-1):
            print(' '*(m-i-1)+'*'+' '*(2*i-1)+'*'+' '*(m-i-1))

        print(' '*(m-1)+'*'+' '*(m-1))
        

    
def P_10():
    perc=float(input('Enter the percentage marks obtn: '))

    if perc>=90:
        print('A')
    elif perc>=80 and perc<=90:
        print('B')
    elif perc>=70 and perc<80:
        print('C')
    elif perc>=60 and perc<70:
        print('D')
    elif perc<=60 and perc>=0:
        print('E')
    else:
        print('Enter a +ve value')
        
r=0
while r==0:
    P_9_4_2()
    r=int(input())



