'''
-> Below code Intuition:-
    -> Use min heap
        -> to track when the apples will be rotten (couldn't think of this way to implement, though idea was the
        same)
    -> in the min heap implementation:-
        -> Based on the rotten day(expiry day earliest)
        -> pushing to heap only when the apples are grown
        -> If the top of heap is expired wrt the day cnt(i) then pop
            -> The loop is maintained in 'or' condition of len(days) and len(heap)
        -> Now if abv criteria failed => an apple can be eaten on ith day
'''

import heapq
class Solution:
    def eatenApples(self, apples: list[int], days: list[int]) -> int:
        res = 0
        i = 0

        min_heap = []

        while i < len(days) or min_heap:
            if i < len(days) and apples[i] > 0:
                heapq.heappush(min_heap,[i+days[i],apples[i]])

            while min_heap and (min_heap[0][0] <= i or min_heap[0][1] <= 0):
                heapq.heappop(min_heap)

            if min_heap:
                min_heap[0][1] -= 1
                res += 1

            i+= 1

        return res

sol = Solution()
print(sol.eatenApples(apples = [1,2,3,5,0,2], days = [3,2,1,4,0,2]))