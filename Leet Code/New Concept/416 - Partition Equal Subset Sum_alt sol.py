'''
-> My sol:-
    -> Improvised on the template of Knapsack without profit

-> This sol:-
    -> Has a better rec:-
        -> Find all possible subarray sums
        -> if sum//2 in dp => T else F
    -> Algo:-
        -> Use set to record the seen subarray sums so far in order to avoid re-computation
        -> add 0 to set bef O(n*w) iteration to record for all individual sum
            -> w is the # of possible subarray sums
'''
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums)%2 != 0:
            return False

        target = sum(nums)//2
        seen_sum = {0}

        for num in nums:
            possible_sums = list(seen_sum)
            for possible_sum in possible_sums:
                seen_sum.add(possible_sum+num)

        return True if target in seen_sum else False

sol = Solution()
print(sol.canPartition([5,1,11,5]))
print(sol.canPartition([1,2,3,4]))
print(sol.canPartition([1,2,3,5]))


