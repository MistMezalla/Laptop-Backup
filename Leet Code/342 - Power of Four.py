class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # return n > 0 and 4**15 % n == 0
        if n <= 0:
            return False

        while n:
            if n > 1 and n % 4 != 0:
                return False
            n //= 4

        return True