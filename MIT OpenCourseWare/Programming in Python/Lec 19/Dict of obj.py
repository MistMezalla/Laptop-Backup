class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def __str__(self):
        return 'Name: '+str(self.name)+'\tand\tAge: '+str(self.age)


L = [2, -5, 'a', 7, (6, 10)]

d = {}

for i in range(0, len(L)):
    if type(L[i]) is int and L[i] >= 0:
        d[L[i]] = Animal(L[i])

# print(d)
for n, a in d.items():
    print(f'key {n} with val {a}')
'''
Line 20 makes use of formatted string.
Some of its examples apart form dict usage are as follows:-

1. Integers
x = 10
y = 20
print(f'x is {x} and y is {y}')
# Output: x is 10 and y is 20

2.Strings
name = "Alice"
greeting = "Hello"
print(f'{greeting}, {name}!')
# Output: Hello, Alice!

3.Floats
pi = 3.14159
print(f'The value of pi is approximately {pi:.2f}')
# Output: The value of pi is approximately 3.14

4.Lists 
my_list = [1, 2, 3]
print(f'My list: {my_list}')
# Output: My list: [1, 2, 3]

*Imp 
The formatted string type is sort of extension of older versions of format specifiers
'''
