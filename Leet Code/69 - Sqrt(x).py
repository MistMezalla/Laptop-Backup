class Solution:
    def mySqrt(self, x: int) -> int:
            if x < 0:
                raise ValueError("Cannot compute square root of a negative number")
            if x == 0 or x == 1:
                return x

            hi = x
            lo = 0

            while (hi - lo) > 1:
                mid = (lo + hi) // 2
                if 0 <= x - mid * mid < 1:
                    return mid
                if mid * mid < x:
                    lo = mid
                else:
                    hi = mid

            return lo

sol = Solution()
print(sol.mySqrt(4))
print(sol.mySqrt(8))
print(sol.mySqrt(9))
