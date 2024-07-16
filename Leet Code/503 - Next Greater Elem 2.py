from collections import deque
class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack = deque()
        queue = deque()
        nge = [-1]*len(nums)

        for i in range(len(nums)):
            while(len(stack) != 0 and nums[i] > nums[stack[-1]]):
                nge[stack[-1]] = nums[i]
                stack.pop()

            queue.appendleft(i)
            stack.append(i)

        for i in range(len(queue)):
            val = nums[queue.pop()]

            while (val > nums[stack[-1]]):
                nge[stack[-1]] = val
                stack.pop()

        return nge

sol = Solution()
print(sol.nextGreaterElements([1,2,3,4,3,1,2]))
print(sol.nextGreaterElements([1,2,3,4,3,2,5,7,1,2,3,4,3]))
print(sol.nextGreaterElements([5,4,3,2,1]))
