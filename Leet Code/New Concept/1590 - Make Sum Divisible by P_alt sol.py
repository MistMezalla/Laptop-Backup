'''
-> Description:-
    -> This is a very good qn based on:-
        -> Hashing
        -> prefix sum
        -> and properties of modulo (little mathematical touch)

-> Intuition:-
    -> newSum = Tot_sum - Sum_Subarr_tbd
        -> taking modulo p on both sides
        -> newSum%p = Tot_Sum %p - Sum_Subarr_tbd
            -> LHS = 0 by prob def
            -> Tot_Sum % p = rem
        -> Thus, Sum_Subarr_tbd = rem, upon solving the eqn
    -> for any subarray, modulo of the sum of subarry bef and aft removal of subarr_tbd rem same
        -> For this we use the concept of hashing wherein we find the starting pt of the subarr_tbd by using this
        abv prop to find the modulo by removing the rem of the enitre subarr from the curr subarr to get the desired
        subarr.
    -> For better visuals see CS(Python 2) NB.
'''
class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        pf_sum = 0
        rem = sum(nums) % p
        subarr_rem_ind = {0: -1}
        if rem == 0:
            return 0

        min_len = float('inf')
        for i,num in enumerate(nums):
            pf_sum += num
            curr_rem = pf_sum % p
            target_rem = (curr_rem - rem + p) % p

            if target_rem in subarr_rem_ind:
                min_len = min(min_len,i - subarr_rem_ind[target_rem])

            subarr_rem_ind[curr_rem] = i

        return min_len if min_len < len(nums) else - 1

