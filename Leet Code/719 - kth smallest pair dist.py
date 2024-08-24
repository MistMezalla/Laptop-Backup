class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        nums.sort()

        def kth_dist(dist):
            cnt = 0
            j = 1
            for i in range(len(nums)):
                while j<len(nums) and nums[j] - nums[i] <= dist: #This method so called overshoots
                    j+=1
                cnt += j-i-1

            # i = 0
            # for j in range(1,len(nums)):
            #     if nums[j] - nums[i] > dist: #This the eff one
            #         i+=1
            #     cnt += j - i

            return cnt

        lo = 0
        hi = nums[-1] - nums[0]

        while hi - lo > 0:
            mid = (hi + lo)//2

            cnt = kth_dist(mid)
            if cnt<k:
                lo = mid + 1
            else:
                hi = mid

        return lo

sol = Solution()
print(sol.smallestDistancePair([1,3,1],1))
print(sol.smallestDistancePair([1,1,1],2))
print(sol.smallestDistancePair([1,6,1],3))
print(sol.smallestDistancePair([1,4,10],1))
print(sol.smallestDistancePair([2,2,0,1,1,0,0,1,2,0],2)) #fails this test case

