class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        pow = abs(n)

        while (pow):
            if pow & 1:
                ans = ans * x
            x *= x
            pow >>= 1

        if n>=0:
            return ans
        else:
            return 1/ans



sol = Solution()
print(sol.myPow(2.000,-3))
print(sol.myPow(2.000,10))
print(sol.myPow(-2.000,9))


