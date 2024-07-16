'''
-> The solution to this problem is of O(sqrt(c)log(c))
-> Hence my approch of O(log c) failed many test cases
'''
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        def first_num(num):
            lo = 0
            hi = num

            while hi - lo > 1:
                mid = (hi + lo)//2

                if mid*mid<=num:
                    lo = mid
                else:
                    hi = mid - 1

            if hi * hi == num:
                return hi
            return lo

        def second_number(num):
            lo = 0
            hi = num

            while hi - lo > 1:
                mid = (hi + lo) // 2

                if mid * mid <= num:
                    lo = mid
                else:
                    hi = mid - 1

            if lo * lo == num:
                return True
            if hi*hi == num:
                return True

            return False

        return second_number(c-first_num(c)**2)

sol = Solution()
print(sol.judgeSquareSum(25))

