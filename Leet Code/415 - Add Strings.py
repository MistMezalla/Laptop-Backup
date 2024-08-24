class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1

        res = ""
        while i > -1 or j > -1 or carry:
            if i >= 0:
                carry += ord(num1[i]) - ord('0')
                i -= 1

            if j >= 0:
                carry += ord(num2[j]) - ord('0')
                j -= 1

            res = chr(carry % 10 + ord('0')) + res
            carry //= 10

        return res


sol = Solution()
print(sol.addStrings('1','9'))
print(sol.addStrings('0','0'))
print(sol.addStrings('9','99'))
print(sol.addStrings('6994','36'))