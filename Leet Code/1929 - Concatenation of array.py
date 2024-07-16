class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        res = []

        for i in range(2*len(nums)):
            res.append(nums[i%len(nums)])

        return res

sol = Solution()
print(sol.getConcatenation([1,2,1]))
print(sol.getConcatenation([1,3,2,1]))
