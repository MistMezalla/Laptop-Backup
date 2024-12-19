'''
-> PLz check for the editorial and the supplementary material for this qn
'''

from collections import deque
class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        maxQ = deque()
        minQ = deque()

        st = 0
        cnt = 0

        for end,num in enumerate(nums):
            while maxQ and nums[maxQ[-1]] < num:
                maxQ.pop()
            maxQ.append(end)

            while minQ and nums[minQ[-1]] > num:
                minQ.pop()
            minQ.append(end)

            while maxQ and minQ and nums[maxQ[0]] - nums[minQ[0]] > 2:
                if maxQ[0] < minQ[0]:
                    st = maxQ.popleft() + 1
                else:
                    st = minQ.popleft() + 1

            cnt += end - st + 1

        return cnt