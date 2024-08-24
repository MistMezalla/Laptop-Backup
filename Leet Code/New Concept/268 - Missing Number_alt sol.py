'''
-> The alternate sol makes use of XOR operator and its prop viz
    -> a^a = 0
    -> a^0 = a
    -> XOR is commutative and associative
        -> Here for numbers in nums:
            -> ans = n1^n2^...nn+1
            -> and when ^ed with numbers from [0,n] then only the missing number will be left out as ans rest will
            be ^ed to 0.
'''

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        ans = 0
        for i in range(len(nums) + 1):
            ans ^= i

        for num in nums:
            ans ^= num

        return ans