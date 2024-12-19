'''
-> Sliding window approach (rather reverse iteration and one pass precomputation)
'''
class Solution:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        n = len(nums)
        max_reach = [0]*n

        max_reach[-1] = n-1

        for i in range(n-2,-1,-1):
            if ((nums[i]&1) + (nums[i+1]&1)) & 1:
                max_reach[i] = max_reach[i+1]
            else:
                max_reach[i] = i

        res = []
        for st,end in queries:
            if max_reach[st] >= end:
                res.append(True)
            else:
                res.append(False)

        return res

sol = Solution()
print(sol.isArraySpecial([2,1],[[0,1]]))



