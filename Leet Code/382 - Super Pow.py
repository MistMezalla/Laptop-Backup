class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        b = [str(i) for i in b]
        n = int("".join(b))  # converting list into integer

        n %= 1140
        a %= 1337

        if n == 0:
            n = 1140

        ans = 1
        while n:
            if n & 1:
                ans = (ans * a) % 1337
            a = (a * a) % 1337
            n >>= 1
        return ans

