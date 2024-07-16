def calcPow(base,expo):
    result=base**expo
    return(result)

base=float(input('Enter the base:' ))
expo=float(input('Enter the exponent: '))

if base>0 and base!=1 :
    print(calcPow(base,expo))

else :
    print('undefined')
