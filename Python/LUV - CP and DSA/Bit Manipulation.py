'''
All the bit operators of c++ resemble with that of python
'''

a = 13
print(a)
print(int(bin(a),2))
print(bin(a))

a = a | 1<<1
print(bin(a))

a = a & ~(1<<2)
print(bin(a))

