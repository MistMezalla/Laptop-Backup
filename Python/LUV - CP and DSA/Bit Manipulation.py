'''
All the bit operators of c++ resemble with that of python
'''

# a = 13
# print(a)
# print(int(bin(a),2))
# print(bin(a))
#
# a = a | 1<<1
# print(bin(a))
#
# a = a & ~(1<<2)
# print(bin(a))

# Method to chk if ith bit is set or unset
a = int("101101",2)
print(a)
set_bit_chker = 1 << 3
print(True if a & set_bit_chker else False)

# Method to get string of i 1's
a = 1 << 2
a = a - 1
print(bin(a))

# Method to unset ith bit
a = int("10111011",2)
unset_bit_maker = ~(1<<3)
print(bin(unset_bit_maker))
a = a & unset_bit_maker
print(True if a & set_bit_chker else False)

# Method to set ith bit
a = int("10110011",2)
set_bit_maker = (1<<3)
print(bin(set_bit_maker))
a = a | set_bit_maker
print(bin(a))
print((type(bin(a))))
print(True if a & set_bit_chker else False)

# Method to toggle ith bit
a = int("10110011",2)
print(bin(a ^ (1 << 0)))



