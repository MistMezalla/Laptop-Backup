class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def ship_weight(max_weight: int):
            num_ships = 1
            curr_sum = 0

            for w in weights:
                if curr_sum + w > max_weight:
                    curr_sum = w
                    num_ships += 1
                    if num_ships > days:
                        return False
                else:
                    curr_sum += w

            return True

        lo, hi = max(weights),sum(weights)

        while hi - lo > 1:
            mid = (hi+lo)//2

            if ship_weight(mid):
                hi = mid
            else:
                lo = mid + 1

        if ship_weight(lo):
            return lo
        else:
            return hi

sol = Solution()
print(sol.shipWithinDays([1,2,3,4,5,6,7,8,9,10],5))
print(sol.shipWithinDays([3,2,2,4,1,4],3))
print(sol.shipWithinDays([1,2,3,1,1],4))
