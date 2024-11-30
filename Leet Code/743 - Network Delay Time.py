import heapq
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj_list = {key:[] for key in range(1,n+1)}

        for u,v,w in times:
            adj_list[u].append((v,w))

        d = {key: float('inf') for key in range(1,n+1)}
        d[k] = 0
        min_heap = [(0,k)]

        while min_heap:
            curr_time,node = heapq.heappop(min_heap)

            if curr_time > d[node]:
                continue

            for neighbour,wt in adj_list[node]:
                time = curr_time + wt

                if time < d[neighbour]:
                    d[neighbour] = time
                    heapq.heappush(min_heap,(time,neighbour))

        curr_max = float('-inf')

        for key,val in d.items():
            if val == float("inf"):
                return -1

            curr_max = max(val,curr_max)

        return curr_max

sol = Solution()
print(sol.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))
print(sol.networkDelayTime(times = [[1,2,1]], n = 2, k = 1))
print(sol.networkDelayTime(times = [[1,2,1]], n = 2, k = 2))