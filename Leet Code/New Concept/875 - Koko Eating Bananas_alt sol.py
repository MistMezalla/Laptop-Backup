class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def can_finish(k):
            hrs = 0
            for pile in piles:
                hrs += (pile+k-1)//k #mathematical alternative to ceil(pile/k)

            return hrs <= h

        lo = 1
        hi = max(piles)

        while hi-lo>1:
            mid = (hi+lo)//2

            if can_finish(mid):
                hi = mid
            else:
                lo = mid + 1

        if can_finish(lo):
            return lo
        else:
            return hi

