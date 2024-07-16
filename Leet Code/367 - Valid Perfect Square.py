class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo = 0
        hi = num

        while hi - lo > 1:
            mid = (hi + lo)//2

            if mid*mid <= num:
                lo = mid
            else:
                hi = mid - 1

        if lo*lo == num:
            return True
        if hi*hi == num:
            return True

        return False
