class Fraction(object):
    def __init__(self, n, d):
        self.num = n
        self.den = d
        self.reduced()

    def reduced(self):
        def gcd(n, d):
            while (d):
                (d, n) = (n % d, d)
            return n
        if(self.den == 0):
            return None
        elif (self.den == 1):
            self.num, self.den = self.num, 1
        else:
            gcd_val = gcd(self.num, self.den)
            self.num //= gcd_val
            self.den //= gcd_val


    def __str__(self):
        if(self.den == 1):
            return str(self.num)
        '''
        if (self.gcd(self.num,self.den) != 1):
           return self.reduced()
        '''
        return str(self.num) + '/' + str(self.den)

    def mul(self, fr):
        return (self.num * fr.num) / (self.den * fr.den)

    def __mul__(self, fr):
        return Fraction(self.num * fr.num, self.den * fr.den)

    def inverse(self):
        self.num, self.den = self.den, self.num

    def get_inverse(self):
        return Fraction(self.den, self.num)

frac1 = Fraction(1,2)
print(frac1)
frac2 = Fraction(3,4)
print(frac2)

frac3 = frac1.mul(frac2)
frac4 = frac1 * frac2
print("Frac3: ", frac3)
print("Frac4: ", frac4)

frac5 = frac2.get_inverse()
print("Frac5: ",frac5)
frac6 = (frac5 * frac2)
print("Frac6: ",frac6)
frac7=Fraction(6,8)
print("Frac7: ",frac7)
frac8 = frac4 * frac5
print("Frac8: ",frac8)