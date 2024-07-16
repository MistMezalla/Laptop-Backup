'''
=> Failed miserably due to the following reasons:-
1. Didn't go by basics
-> didn't form a proper predicate function as just tried to improve on the predicate functions of Q875 and Q1552
2. Tried to solve in ana approach only
-> sorted the arr which was not req wrt problem statement
-> Hence the predicate function formation was derailed from right solution
'''
class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def can_split(Sum: int):
            sub = k
            pos_split = 0
            i = 0
            while i < len(nums):
                s = 0
                while i<len(nums) and s<=Sum:
                    s += nums[i]
                    i+=1

                if s >= Sum:
                    sub -= 1
                    if i != len(nums):
                        pos_split = i

                if sub == 0:
                    break

            if sub == 0:
                return pos_split
            else:
                return len(nums)




        nums.sort()
        lo = 0
        hi = sum(nums)

        while (hi - lo)>1:
            mid = (hi + lo)//2

            if can_split(mid) < len(nums):
                lo = mid
            else:
                hi = mid - 1

        if can_split(hi) < len(nums):
            return sum(nums[can_split(hi):])
        else:
            return sum(nums[can_split(lo):])

sol = Solution()
print(sol.splitArray([5,7,8,2,10],2))
