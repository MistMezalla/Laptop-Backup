'''
-> Well some of the areas where my sol failed is that:-
    -> for intermediate stops from src to dest the d[node/neighbour] nit updated properly as the corresponding nodes/
    neighbours were updated already to a val lesser than the curr_val
        -> for clarity on the abv pt try to dry run my sol onto marked test case in my sol

-> so instead of mapping <int> : <int> for d
    -> here we will map <tuple>:<int> ; where tuple is <node,stops taken to reach from src node>
'''

import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adj_list = {key: [] for key in range(n)}

        for u,v,wt in flights:
            adj_list[u].append((v,wt))

        d = {(key,0):float("inf") for key in adj_list}
        d[(src,0)] = 0
        min_heap = [(0,src,0)] # cost,node,stops

        while min_heap:
            curr_cost,node,stops = heapq.heappop(min_heap)

            if node == dst:
                return curr_cost

            if stops > k:
                continue

            for neighbour,wt in adj_list[node]:
                new_cost = curr_cost + wt

                if new_cost < d.get((neighbour,stops+1),float("inf")):
                    d[(neighbour,stops+1)] = new_cost
                    heapq.heappush(min_heap,(new_cost,neighbour,stops+1))

        return -1

sol = Solution()
print(sol.findCheapestPrice( n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1))
print(sol.findCheapestPrice(4,[[0,1,1],[0,2,5],[1,2,1],[2,3,1]],0,3,1))
# My sol fails for this test case
print(sol.findCheapestPrice(5,[[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]],0,2,2))

