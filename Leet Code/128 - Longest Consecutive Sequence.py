class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        max_len = float('-inf')

        for num in num_set:
            if num - 1 not in num_set:
                curr_num = num
                curr_len = 1

                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_len += 1

                max_len = max(max_len, curr_len)

        return max_len

sol = Solution()
print(sol.longestConsecutive([100, 1, 200, 3, 5]))
