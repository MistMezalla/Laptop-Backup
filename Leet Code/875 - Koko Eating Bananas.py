'''
-> This approach gives TLE due to while nested inside a for loop
-> Hence should have used the formula :  hrs += ceil(piles[i]/k) to calculate the total number of taken
'''
from math import ceil
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def is_true(k):
            hrs = 0
            for i in range(len(piles)):
                hrs += ceil(piles[i]/k)

            return hrs <= h

        lo = 1
        hi = max(piles)

        while (hi-lo)>1:
            mid = (hi+lo)//2

            if is_true(mid):
                hi = mid
            else:
                lo = mid + 1

        if is_true(lo):
            return lo
        else:
            return hi

sol =  Solution()
print(sol.minEatingSpeed([3,6,7,11],8))