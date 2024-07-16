'''
def numbercheck(num):
    assert(num>=0) , "OOPS.... Negative Number"
    print(num**2)

print(numbercheck(-100))
print(numbercheck(100))
'''
def numcheck(n):
    assert(n>=0) , "OOPS.... Negative Number"
    print(n**2)

t=int(input('Enter any integer: '))

if t>=0:
    print(numcheck(t))
else:
    print(numcheck(t))

'''IN funtion numcheck since it is given print statement and no retturn statement
is written to give any specified value for this function call, hence 49
and none both are printed'''

