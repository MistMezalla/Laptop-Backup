class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            if n & 1:
                cnt += 1
            n = n >> 1

        return cnt

sol = Solution()
print(sol.hammingWeight(1))
print(sol.hammingWeight(128))
print(sol.hammingWeight(2147483645))
