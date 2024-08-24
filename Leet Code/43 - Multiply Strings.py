class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return self.num_to_str(self.Karatsuba(self.str_to_num(num1),self.str_to_num(num2)))

    def Karatsuba(self,num1,num2):
        if num1 < 10 or num2 < 10:
            return num1 * num2

        num1 = self.num_to_str(num1)
        num2 = self.num_to_str(num2)
        m = max(len(num1),len(num2))//2

        a1,a0 = self.str_to_num(num1[:-m]),self.str_to_num(num1[-m:])
        b1,b0 = self.str_to_num(num2[:-m]),self.str_to_num(num2[-m:])

        z0 = self.Karatsuba(a0,b0)
        z1 = self.Karatsuba((a1 + a0),(b1 + b0))
        z2 = self.Karatsuba(a1,b1)

        return z2 * 10 ** (2*m) + (z1 - z0 - z2) * 10 ** m + z0

    def str_to_num(self,num: str):
        base = 1
        #num = num[::-1]
        number = 0
        for i in range(len(num)):
            number += (ord(num[len(num) - 1 - i]) - ord('0')) * base
            base *= 10

        return number

    def num_to_str(self,num: int):
        res = ""
        if num == 0:
            return '0'
        while num:
            dig = num % 10
            num //= 10
            res = chr(dig + ord('0')) + res

        return res




sol = Solution()
print(sol.multiply('6','5'))
print(sol.multiply('9','999'))
print(sol.multiply('0','10021231654'))




