from collections import deque
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nge_nums2 = [-1]*len(nums2)
        stack = deque()
        hash = {}

        for i in range(len(nums2)):
            while(len(stack) != 0 and nums2[i]>=nums2[stack[-1]]):
                nge_nums2[stack[-1]] = nums2[i]
                stack.pop()

            stack.append(i)
            hash[nums2[i]] = i

        ans = []
        for i in range(len(nums1)):
            ans.append(nge_nums2[hash[nums1[i]]])

        return ans






sol = Solution()
print(sol.nextGreaterElement([4,1,2],[1,3,4,2]))
print(sol.nextGreaterElement([2,4],[1,2,3,4]))
print(sol.nextGreaterElement([3],[1,2,4,3]))
