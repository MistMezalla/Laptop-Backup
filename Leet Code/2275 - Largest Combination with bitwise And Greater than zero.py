class Solution:
    def largestCombination(self, candidates: list[int]):
        bit_cnt = [0] * 24

        for i in range(24):
            for num in candidates:
                if (num >> i) & 1:
                    bit_cnt[i] += 1

        return max(bit_cnt)

sol = Solution()
print(sol.largestCombination([8,8]))
print(sol.largestCombination([16,17,71,62,12,24,14]))
print(sol.largestCombination([16,17,8,9,13,15,10]))
        