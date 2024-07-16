# 1:-math module
import math
num1=10.34
num2=-8.17

# 1.1:-math.ceil
print(math.ceil(num1))
print(math.ceil(num2))
#returns the smallest integer to the right of given num on wrt number line

# 1.2:-math.floor
print(math.floor(num1))
print(math.floor(num2))
#returns the greatest integer to the left of given num on wrt number line

# 1.3:-math.fmod
print(math.fmod(10,25))
print(math.fmod(25,10))
print(math.fmod(-10,25))
print(math.fmod(-25,10))
print(math.fmod(-25,-10))
print(int(math.fmod(10,25)))

# 1.4:-math.trigo
print(math.tan(0))

# 1.5:-math.log
print(math.log(2,10))

# 2:- rmdom modu8le
import random

print(random.random())

print(random.randrange(-6,7))

# 3:- From Statement

from math import log,ceil
from random import randrange
a=randrange(1,10)
x=log(a,10)
x=ceil(x)
print(x)

# 4:- Built in functions

print(divmod(4,8))
#print(float(divmod(50,7))) #TypeError: float() argument must be a string or a number, not 'tuple'

#print(max({12,3456789,'good morning'})) #TypeError: '>' not supported between instances of 'int' and 'str'

str1='Hello'

print(str1.upper())
