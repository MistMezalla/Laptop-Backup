class Solution:
    def minDeletion(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1

        prev_del = False
        op = 0
        for i in range(0,len(nums),2):
            if not prev_del:
                if i+1 < len(nums) and nums[i] == nums[i+1]:
                    op += 1
                    prev_del = True

            if prev_del:
                if nums[i] == nums[i-1]:
                    op += 1
                    prev_del = False

        return op 

sol = Solution()
print(sol.minDeletion(nums = [1,1,2,3,5]))
print(sol.minDeletion(nums = [1,1,2,2,3,3]))
print(sol.minDeletion([2,2,2]))
print(sol.minDeletion([1,1,2,2,3,3,3,7,7]))
print(sol.minDeletion([1,1,4,2,2,5,3,3,3,6]))


