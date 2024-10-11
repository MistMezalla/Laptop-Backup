'''
-> My Intuition:-
    -> Target value(val where all vals of array will coincide) belongs to one of the values from range [min,max]
    -> Bin search to find the target value
        -> However cldn't come up with eff strategy to make use of bin search

-> Below code Intuition:-
    -> Bin search
        -> When u carry out cost calc for each integral val in range [min,max] then we will see kind of parabolic
        upward nature of values of cost associated to each target val.
        -> Bin search to find the deepest pt of this curve so formed.
'''
class Solution:
    def minCost(self, nums: list[int], cost: list[int]) -> int:
        def target_cost(target):
            tot_cost = 0
            for i in range(len(nums)):
                tot_cost += abs(target - nums[i]) * cost[i]

            return tot_cost

        lo = min(nums)
        hi = max(nums)

        while (hi - lo) > 0:
            mid = (hi + lo)//2

            if target_cost(mid) < target_cost(mid + 1):
                hi = mid
            else:
                lo = mid + 1

        return target_cost(lo)

sol = Solution()
print(sol.minCost(nums = [1,3,5,2], cost = [2,3,1,14]))
print(sol.minCost(nums = [2,2,2,2,4], cost = [4,2,8,1,3]))


