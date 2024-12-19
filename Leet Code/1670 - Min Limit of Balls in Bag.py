from math import ceil
class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        hi,lo = max(nums),1

        while hi - lo > 0:
            mid = (hi + lo)//2

            if self.is_min(maxOperations,mid,nums):
                hi = mid

            else:
                lo = mid + 1

        return lo

    def is_min(self,max_op,max_balls,nums):
        curr_op = 0

        for num in nums:
            curr_op += ceil(num/max_balls) - 1

            if curr_op > max_op:
                return False

        return True

sol = Solution()
print(sol.minimumSize(nums = [9], maxOperations = 2))
print(sol.minimumSize(nums = [2,4,8,2], maxOperations = 4))