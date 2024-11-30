import heapq
class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int,
                       end_node: int) -> float:
        adj_list = {key:[] for key in range(n)}

        for ind,(u,v) in enumerate(edges):
            adj_list[u].append([v,succProb[ind]])
            adj_list[v].append([u,succProb[ind]])

        d = {key:0 for key in range(n)}
        d[start_node] = 1
        max_heap = [(-1,start_node)]

        while max_heap:
            curr_prob,node = heapq.heappop(max_heap)
            curr_prob *= -1

            if curr_prob < d[node]:
                continue

            for neighbour,p in adj_list[node]:
                probability = curr_prob * p

                if probability > d[neighbour]:
                    d[neighbour] = probability
                    heapq.heappush(max_heap,(-probability,neighbour))


        return d[end_node]

sol = Solution()
print(sol.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start_node = 0, end_node = 2))
print(sol.maxProbability(n = 3, edges = [[0,1]], succProb = [0.5], start_node = 0, end_node = 2))