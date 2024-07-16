def P_6_3():
    n1=float(input('Enter the 1st number: '))
    n2=float(input('Enter the 2nd number: '))
    op=input('Enter the operation to be executed: ')

    if op=='+':
        res=n1+n2
        print(res)
    elif op=='-':
        from math import fabs
        res=n1-n2
        print(fabs(res))
    elif op=='*':
        res=n1*n2
        print(res)
    elif op=='/':
        if n2==0:
            print('Division Error: Enter number other\
than zero')
        else:
            res=n1/n2
            print(res)

def P_6_8():
    t=0
    l_1=[1,3,5,7]
    '''
    while t==0:
        var=int(input('Enter the number: '))
        l.append(var)
        t=int(input())
    '''
    l_2=[]
    
    for i in l_1:
        if i%2==0:
            l_2.append(i)
        else:
            continue
    if len(l_2)==0:
        print('no even number')
    else:
        print(l_2)

def P_6_11():
    num=float(input('Enter the number: '))
    l=[]
    for i in range(1,int(num/2)+1):
        if num%i==0:
            l.append(float(i))
    l.append(num)

    print(l)

def P_6_13():
    total=0
    while True:
        num=float(input('Enter the number: '))
        if num>=0:
            total+=num
        else:
            break
    
    print(total)

def P_6_14():
    num=float(input('Enter the number: '))

    if num>1 or (num<1 and num>0):
        from math import sqrt,ceil
    
        for i in range (2,int(ceil(sqrt(num)))+1):
            if num%i==0:
                t=1
                break
            else:
                t=2

        if t==1:
            print('Composite')
        elif t==2:
            print('prime')

    elif num==1:
        print('Neither prime nor composite')

    else:
        print('Enter a whole number')

def P_6_17():
    num=int(input('Enter the number: '))

    for i in range(1,num + 1):
        for j in range(1,i+1):
            print(j,end=' ')
        print()

def P_6_18():
    l=[]
    for i in range(2,51):
        t=1
        #Note:-
        "If t=1 wasn't written, then 't' in the below 'for\
        block' wld hv become local which thereby couldn't\
        hv been able to use the same in below statement of\
        't==2'"
        for j in range(2,i+1):
            if i!=j:
                if i%j==0:
                    t=1
                    break
                else:
                    t=2
            elif i==j:
                continue
            
        if t==2:
            l.append(i)

    print(l)

def P_6_19():
    num=int(input('enter the number whose factorial is \
to be found'))
    fact=1
    if num>0:
        for i in range(num,0,-1):
            fact*=i
        print(fact)
    elif num==0:
        print(fact)
    else:
        print('Enter a positive number')
    

r=0
while r==0:
    P_6_19()
    r=int(input())        




        
        
        
