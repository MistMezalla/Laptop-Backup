'''
-> My Intuition:-
    -> Tried to use NGE template
        -> cldn't modify for the problem specifications
    -> Tried to use 2 ptrs(ptrs placed at extreme ends)
        -> cldn't come up with robust conditions to handle all test and edge cases

-> Below sol:-
    -> This sol makes use of concept of "monotonic stack"
        -> Plz refer supplementary material for this qn to understand basics abt the term 'monotonic stack"

    -> This algo first forms a decreasing monotonic stack in one forward linear pass
    -> Subsequently it makes another linear pass in reverse order while taking the help of decr mono stack formulated
    to find the max width
    -> So wrt NGE problems here 2 passes were made:-
        -> 1st to form mono st
        -> then to make use of the stack so formed
    rather all done in single pass in case of NGE.
'''

from collections import deque
class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        stack = deque()

        for i in range(len(nums)):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)

        max_width = 0
        for i in range(len(nums) -1,-1,-1):
            while stack and nums[stack[-1]] <= nums[i]:
                max_width = max(max_width,i - stack.pop())

        return max_width
