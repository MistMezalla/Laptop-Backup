'''
basic_math Module

performs the basic arithematic operations on the given two numbers in the given order.
'''

def addnum(x,y):
    return(x+y)

def subnum(x,y):
    return(x-y)

def  multnum(x,y):
    return(x*y)

def divnum(x,y):
    if y==0:
        print('division by zero error')

    else:
        return(x/y)



