x#Solved Programs
def P_7_1():
    st=input('Enter a welcome message: ')
    print(st)
    print(input('Enter a welcome message: '))

def P_7_3():
    l=float(input('Enter the length of the rectange: '))
    b=float(input('Enter the breadth of the rectange: '))
    area=l*b
    print('Area of the rectangle is',area)

def P_7_4():
    w=float(input('Enter your weight in kg: '))
    h=float(input('Enter your height in m: '))
    BMI=w/h**2
    print('Your BMI is',BMI)

def P_7_6():
    val_km=float(input('Enter the value in km: '))
    val_mile=val_km*0.621371
    print('The value in miles is',val_mile)

def P_7_9():
    n1=float(input('Enter the 1st number: '))
    n2=float(input('Enter the 2nd number: '))
    n1,n2=n2,n1
    print(n1,n2)
    
def P_7_10():
    n1=float(input('Enter the 1st number: '))
    n2=float(input('Enter the 2nd number: '))
    n3=float(input('Enter the 3rd number: '))

    n1,n2,n3=n2,n3,n1
    print(n1,n2,n3)
    
P_7_10()


    



