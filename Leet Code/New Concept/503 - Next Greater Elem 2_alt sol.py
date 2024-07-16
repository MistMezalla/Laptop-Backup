'''
-> This version avoids the need for a separate queue and handles the circular nature directly by iterating up to 2*n.
'''

from collections import deque
class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack = deque()
        nge = [-1]*len(nums)

        for i in range(2*len(nums)):
            while(len(stack) != 0 and nums[i%len(nums)] > nums[stack[-1]]):
                nge[stack.pop()] = nums[i % len(nums)]

            if i<len(nums):
                stack.append(i)

        return nge

sol = Solution()
print(sol.nextGreaterElements([1,2,3,4,3,1,2]))
print(sol.nextGreaterElements([1,2,3,4,3,2,5,7,1,2,3,4,3]))
print(sol.nextGreaterElements([5,4,3,2,1]))


