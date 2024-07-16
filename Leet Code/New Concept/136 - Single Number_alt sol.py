'''
Used the properties of Bit XOR operator. See my NB for more,i.e, for the proof of the algo.
'''
class Solution(object):
    def singleNumber(self, nums: list[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            ans ^= nums[i]
        return ans

my_sol = Solution()
print(my_sol.singleNumber([3,4,1,7,2,1,2,4,3,7]))