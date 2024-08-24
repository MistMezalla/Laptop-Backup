class Solution:
    def specialArray(self, nums: list[int]) -> int:
        lo, hi = 0,len(nums)

        def Count(val):
            cnt = 0
            for num in nums:
                if num >= val:
                    cnt += 1

            return cnt

        while hi - lo > -1:
            mid = (hi + lo)//2

            if Count(mid) == mid:
                return mid
            elif  Count(mid) > mid:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1

sol = Solution()
print(sol.specialArray([0,4,0,3,4]))
print(sol.specialArray([0,0]))
print(sol.specialArray([0,2,1,0,3]))

