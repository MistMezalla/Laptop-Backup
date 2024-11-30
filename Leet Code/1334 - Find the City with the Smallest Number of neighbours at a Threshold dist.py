'''
-> well an experimental dfs on each node based approach failed on test case highlighted below
-> hence use SSSP algo on each node to solve such qns
'''
import heapq
class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        # smallest_city = -1
        # num_cities = 1000
        # adj_list = [[] for _ in range(n)]
        #
        # for u,v,wt in edges:
        #     adj_list[u].append([v,wt])
        #     adj_list[v].append([u,wt])
        #
        # for city in range(n):
        #     visited = [0] * n
        #     num_cities_reachable = 0
        #
        #     def dfs(node,curr_len):
        #         visited[node] = 1
        #         nonlocal num_cities_reachable
        #         for neighbour,weight in adj_list[node]:
        #             if not visited[neighbour]:
        #                 if curr_len + weight > distanceThreshold:
        #                     continue
        #                 num_cities_reachable += 1
        #                 dfs(neighbour,curr_len + weight)
        #
        #     dfs(city,0)
        #
        #     if num_cities_reachable < num_cities:
        #         num_cities = num_cities_reachable
        #         smallest_city = city
        #
        #     elif num_cities_reachable == num_cities:
        #         num_cities = num_cities_reachable
        #         smallest_city = city
        #
        #
        # return smallest_city

        adj_list = {key:[] for key in range(n)}

        for u,v,wt in edges:
            adj_list[u].append([v,wt])
            adj_list[v].append([u,wt])

        smallest_city = -1
        num_cities_reachable = 1000
        for start in range(n):
            d = {key:float("inf") for key in range(n)}
            d[start] = 0
            min_heap = [(0,start)] #dist,node

            while min_heap:
                curr_dist,node = heapq.heappop(min_heap)

                if curr_dist > d[node]:
                    continue

                for neighbour,weight in adj_list[node]:
                    dist = curr_dist + weight

                    if dist < d[neighbour]:
                        d[neighbour] = dist
                        heapq.heappush(min_heap,(dist,neighbour))

            num_cities = -1
            for city in range(n):
                if d[city] <= distanceThreshold:
                    num_cities += 1

            if num_cities <= num_cities_reachable:
                num_cities_reachable = num_cities
                smallest_city = start

        return smallest_city


sol = Solution()
print(sol.findTheCity(n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4))
print(sol.findTheCity(n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2))
print(sol.findTheCity(6,[[0,3,7],[2,4,1],[0,1,5],[2,3,10],[1,3,6],[1,2,1]],417))
# the dfs based sol will fail for this test case:-
print(sol.findTheCity(6,[[0,1,10],[0,2,1],[2,3,1],[1,3,1],[1,4,1],[4,5,10]],20))
