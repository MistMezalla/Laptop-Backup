'''
-> Improvements wrt to my code:-
    -> max_val (max bit or) will rem same even after undergoing several(bit or) opns.
    -> curr_val can be calculated and passed as parameter to the function to avoid O(n) curr_val computation
    -> Another method to for the usage of 'nonlocal' key word for immutable data types
'''
class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        cnt = [0] # substitute usage for nonlocal keyword for immutable types
        max_val = 0
        for num in nums:
            max_val |= num

        def gen_subsets(st,curr_val,max_val,cnt):
            if max_val == curr_val:
                cnt[0] += 1

            for i in range(st,len(nums)):
                gen_subsets(i+1,curr_val | nums[i],max_val,cnt)

        gen_subsets(0,0,max_val,cnt)
        return cnt[0]
