class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        cnt = 0
        less_than = 0
        for num in nums:
            if num ==  target:
                cnt+=1
            elif num < target:
                less_than += 1

        res = []
        for i in range(cnt):
            res.append(less_than)
            less_than += 1

        return res

sol = Solution()
print(sol.targetIndices([1,2,5,2,3],2))
