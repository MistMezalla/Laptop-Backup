'''
-> See Supplementary material for ref.
'''
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = [[]]

        i = 0
        while i < len(nums):
            cnt = 0
            while (i + cnt < len(nums) and nums[i+cnt] == nums[i]):
                cnt+=1

            prev_subsets = len(res)
            for j in range(prev_subsets):
                subset = res[j][:] #list copy(true cpy) to avd ref conflict in case of python
                for k in range(cnt):
                    subset.append(nums[i])
                    res.append(subset[:])

            i += cnt

        return res

sol = Solution()
print(sol.subsetsWithDup([2,1,2]))

