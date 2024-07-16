'''
-> even though below directly using sqrt and expo ops directly but the still take O(log n) time at each call
'''
from math import isqrt,sqrt
class Solution1:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(isqrt(c) + 1):
            b = sqrt(c - a*a)

            if b == int(b):
                return True

        return False

sol = Solution1()
print(sol.judgeSquareSum(25))

class Solution2:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = isqrt(c)

        curr_sum = 0
        while left <= right:
            curr_sum = left*left + right*right

            if curr_sum == c:
                return  True

            if curr_sum < c:
                left += 1
            else:
                right -= 1

        return False

sol = Solution2()
print(sol.judgeSquareSum(3))

