class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == -2**31:
            return True

        n = abs(n)
        cnt = 0
        while n:
            if n & 1:
                cnt+= 1
            if cnt > 1:
                return False
            n = (n >> 1)

        return True
