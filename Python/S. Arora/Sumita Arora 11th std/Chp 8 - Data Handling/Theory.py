#complex numbers
def complex_numbers():
    n1=2+4j
    n2=10
    n3=-5j
    print(n1,n2,n3)

    print(n1.real,n2.real,n3.real)
    print(n1.imag,n2.imag,n3.imag)

def explict_conversions():
    n1=12+14j
    n2=int(n1.real)
    n3=int(n1.imag)
    a,b,c=bin(n2),oct(n2),hex(n2)
    print(a,b,c)
    print()

    "x,y,z=int(a),bin(b),oct(c)\
     print(x,y,z)"
    
    print(int(0b1100))
    print(type(a),type(n2))
    print()

    #Note:-
    "bin(),hex(),oct() return values in 'class str'\
    thus use format, int(<str>,<radix value of the str>)"

    x=int(a,2)
    print(x)
    print()

    "y=bin(b,8)\
     print(y)"

    #Note:-
    "bin(),hex(),oct() take exactly one argument.\
    Thus to convert from say bin to oct, we have to convert\
    the same via int(<str>,<radix>)."

    y=int(b,8)
    y=bin(y)
    print(y)
    print()

    z=int(c,16)
    print(oct(z))
    print()

    print(complex(10))
    print(complex(10,2))
    print(complex(0,-2))
    print(complex(-0,-2))
    print()
           

explict_conversions()
