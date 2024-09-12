'''
-> My Intuition:-
    -> Greedy choice based on:-
        -> wage/qlty
        -> wage
        -> qlty
    -> But individual greedy choices are not sufficient to solve this probelm

-> This code Intuition:-
    -> Greedy choice:-
        -> Sort based on wage/qlty in incr order
        -> build max heap of first k elem of sorted ratio list based on 'qlty' only
        -> substitute the max qlty with rem elem one by one to reduce the overall qlty sum of k elem chosen
        tentatively.
        -> Keep track of the min sum wage during the substitution process

    -> Substitution is done as ratio = wage/qlty => sum_wage = ratio * sum_qlty.
    -> Smaller the sum_qlty smaller will be the LHS.
'''

import heapq
class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        ratio = [(wages/qlty,qlty) for wages,qlty in zip(wage,quality)]

        ratio.sort(key = lambda x: x[0])

        max_heap = []
        qlty_sum = 0
        max_ratio = 0.0
        for i in range(k):
            qlty_sum += ratio[i][1]
            max_ratio = max(max_ratio,ratio[i][0])
            heapq.heappush(max_heap,-ratio[i][1])

        res = max_ratio * qlty_sum

        for i in range(k,len(ratio)):
            max_ratio = max(max_ratio,ratio[i][0])
            qlty_sum += heapq.heappop(max_heap) + ratio[i][1]
            heapq.heappush(max_heap,-ratio[i][1])
            res = min(res,max_ratio*qlty_sum)

        return res

sol = Solution()
print(sol.mincostToHireWorkers(quality = [10,20,5], wage = [70,50,30], k = 2))
print(sol.mincostToHireWorkers( quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3))

