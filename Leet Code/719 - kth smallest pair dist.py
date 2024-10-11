class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        nums.sort() # since written absolute diff hence i am able to sort without messing up with the
                    # constraint of  0 <= i < j < nums.length ; where i and j are indices

        def kth_dist(dist):
            cnt = 0
            j = 1
            for i in range(len(nums)):
                while j<len(nums) and nums[j] - nums[i] <= dist: #This method so called overshoots
                    j+=1
                cnt += j-i-1

            # i = 0
            # for j in range(1,len(nums)):
            #     while nums[j] - nums[i] > dist: #This the eff one
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
            # elif cnt > k:     # this logic is wrong as the logic counts for dist <= mid(here mid may not be a
            #     hi = mid - 1  # valid dist as well.
            # else:             # 2nd reason why hi - lo > 0 works as it is an improvement over hi - lo > 1 as follows
            #     return mid        # in case of 2 elem mid == lo so the predicate value of lo is returned to bin
            else:                   #search logic hence we can thereby safely return eihter hi or lo based on
                hi = mid            # bin search logic and dry run

        return lo

sol = Solution()
print(sol.smallestDistancePair([1,4,2],1))
print(sol.smallestDistancePair([1,1,1],2))
print(sol.smallestDistancePair([1,6,1],3))
print(sol.smallestDistancePair([1,4,10],1))
print(sol.smallestDistancePair([2,2,0,1,1,0,0,1,2,0],2)) #fails this test case

