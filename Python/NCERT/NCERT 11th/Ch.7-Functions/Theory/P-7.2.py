def addnum():
    num1=float(input('Enter the first number'))
    num2=float(input('Enter the second number'))
    sum1=num1+num2
    print('sum of the number entered is', sum1)

def addnum1():
    num1=float(input('Enter the first number'))
    num2=float(input('Enter the second number'))
    sum1=num1+num2
    print('sum of the number entered is', sum1)

addnum1()

#NOTE
'''since fuction addnum wasn't called hence the statements within it weren't
executed even if there was no syntax errro within'''
'''however when the function addnum1 was called in, its statements were executed
though body of addnum and addnum1 function was the same'''
