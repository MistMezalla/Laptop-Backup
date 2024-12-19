class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        for i in range(len(nums)-1):
            t1 = nums[i] & 1
            t2 = nums[i+1] & 1

            if (t1+t2)&1 == 0:
                return False

        return True

sol = Solution()
print(sol.isArraySpecial([4,3,2,1,6,8]))
print(sol.isArraySpecial([8]))