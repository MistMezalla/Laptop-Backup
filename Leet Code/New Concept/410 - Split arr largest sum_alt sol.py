class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def can_split(Sum: int):
            sub_arr = 1
            curr_sum = 0

            for num in nums:
                if curr_sum + num > Sum:
                    curr_sum = num
                    sub_arr += 1
                    if sub_arr > k:
                        return False
                else:
                    curr_sum += num

            return True

        lo, hi = max(nums),sum(nums)
        while hi - lo >1:
            mid = (hi + lo)//2
            if can_split(mid):
                hi = mid
            else:
                lo = mid + 1

        if can_split(lo):
            return lo
        else:
            return hi

sol = Solution()
print(sol.splitArray([7,5,2,10,8],2))