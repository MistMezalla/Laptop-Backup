'''
-> PLz refer supplementary material to understand the intuition behind this code.
'''

from math import ceil
class Solution:
    def minimumFuelCost(self, roads: list[list[int]], seats: int) -> int:
        adj_list = [[] for _ in range(len(roads) + 1)]

        for u,v in roads:
            adj_list[u].append(v)
            adj_list[v].append(u)

        res = 0
        def dfs(prev,node,people = 1):
            nonlocal res
            for next in adj_list[node]:
                if next == prev:
                    continue
                people += dfs(node,next)
            res += int(ceil(people/seats)) if node else 0 # calculating the tot cost to reach from node -> prev

            return people

        dfs(0,0)
        return res

sol = Solution()
print(sol.minimumFuelCost(roads = [[0,1],[0,2],[0,3]], seats = 5))
print(sol.minimumFuelCost([[0,1]],4))
print(sol.minimumFuelCost([[0,1],[1,2],[1,3],[1,4]],2))
print(sol.minimumFuelCost([[0,1],[1,2],[1,3],[1,4],[4,5],[5,7],[5,6],[6,8],[0,9],[9,10],[0,11]],3))
