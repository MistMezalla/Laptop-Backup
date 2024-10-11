'''
-> My Intuition:-
    -> Just improved upon 53 to handle cases of circularity

-> Below code:-
    -> It makes use of the fact that MSA has 2 cases viz
        -> When MSA is not circular
            -> return this MSA
        -> When MSA is circular
            -> => min sum subarray is not circular
            -> hence return total sum - min sum subarray
        -> Handles the case of all -ve arrays as edge case separately
'''
class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        curr_max = total = curr_min = 0
        max_sum = min_sum = nums[0]

        for num in nums:
            curr_max = max(num,curr_max + num)
            max_sum = max(max_sum, curr_max)

            curr_min = min(num,curr_min + num)
            min_sum = min(curr_min,min_sum)

            total += num

        return max(max_sum,total-min_sum) if max_sum >= 0 else max_sum

class Solution_DnC():
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        non_circular_MSA = self.MSA(nums,0,len(nums) - 1)

        min_sum = nums[0]
        total = 0
        curr_min = 0

        for num in nums:
            curr_min = min(num,curr_min+num)
            min_sum = min(curr_min,min_sum)
            total+=num

        if total == min_sum:
            return non_circular_MSA

        return max(non_circular_MSA,total - min_sum)

    def MSA(self,nums,left,right):
        if left>=right:
            return nums[left]

        mid = (left+right)//2

        left_sum = self.MSA(nums,left,mid)
        right_sum = self.MSA(nums,mid+1,right)

        left_suffix = right_prefix = float('-inf')
        curr_sum = 0

        for i in range(mid-1,left-1,-1):
            curr_sum += nums[i]
            left_suffix = max(left_suffix,curr_sum)

        curr_sum = 0
        for i in range(mid+1,right+1):
            curr_sum += nums[i]
            right_prefix = max(right_prefix,curr_sum)

        return max(left_sum,right_sum,left_suffix+nums[mid]+right_prefix)


sol = Solution()
print(sol.maxSubarraySumCircular([1,2,3,4,5]))
print(sol.maxSubarraySumCircular([5,-3,5,1]))
print(sol.maxSubarraySumCircular([5,1,-3,5]))
print(sol.maxSubarraySumCircular([-3,-2,-3]))
print(sol.maxSubarraySumCircular([-3,5,1,-6,7]))

