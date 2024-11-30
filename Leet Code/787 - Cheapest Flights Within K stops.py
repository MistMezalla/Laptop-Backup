import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adj_list = {key: [] for key in range(n)}

        for u, v, w in flights:
            adj_list[u].append((v, w))

        d = {key: float('inf') for key in range(n)}
        d[src] = 0
        min_heap = [(0,src,0)] # cost,node,path_len
        # parent = {key: None for key in range(n)}
        # path_length = [0] * n

        while min_heap:
            curr_cost,node,path_len = heapq.heappop(min_heap)

            if path_len == k + 1:
                continue

            # if curr_cost > d[node]:
            #     continue

            for neighbour,wt in adj_list[node]:
                cost = curr_cost + wt

                if cost < d[neighbour]:
                    # parent[neighbour] = node
                    d[neighbour] = cost
                    heapq.heappush(min_heap,(cost,neighbour,path_len + 1))


        return d[dst] if d[dst] != float('inf') else -1

sol = Solution()
print(sol.findCheapestPrice( n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1))
print(sol.findCheapestPrice(4,[[0,1,1],[0,2,5],[1,2,1],[2,3,1]],0,3,1))
# My sol fails for this test case
print(sol.findCheapestPrice(5,[[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]],0,2,2))

