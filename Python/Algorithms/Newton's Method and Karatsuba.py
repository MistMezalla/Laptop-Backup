'''
-> Bottled in the recursive calls as had to make recursive calls on z0,z1 and z2 whereas I tried to recurse on
a1,a0,b1,b0.
-> Another imp pt is to partition based on max on lengths to ensure uniform higher(upper) half splitting
'''
'''
Revised = 1
Resolved = 1
'''
class Numerics:
    def Karatsuba(self,a: int,b: int):
        if a<10 or b<10:
            return a*b

        a = str(a)
        b = str(b)

        m = max(len(a),len(b))//2

        a1,a0 = int(a[:-m]),int(a[-m:])
        b1,b0 = int(b[:-m]),int(b[-m:])

        z0 = self.Karatsuba(a0,b0)
        z1 = self.Karatsuba((a0 + a1),(b0 + b1))
        z2 = self.Karatsuba(a1,b1)

        return z2*10**(2*m) + (z1-z0-z2)*10**m + z0

num = Numerics()
print(num.Karatsuba(1234,5678))



