'''
-> The below code meticulously makes use of the concepts/algo viz
    -> Kahn's algo
    -> reversal of graphs

-> For more clarity of intuition of code plz refer editorial
    -> basically we are reverse traversing from the terminal node to potential safe nodes
        -> now these potential safe nodes can become safe nodes if these nodes are not part of any cycle
        -> to ensure this we make use of Kahn's algo
'''

from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        rev_adj_list = [[] for _ in range(n)]
        in_degree = [0] * n

        for u in range(n):
            for v in graph[u]:
                rev_adj_list[v].append(u)
                in_degree[u] += 1

        queue = deque([node for node in range(n) if in_degree[node] == 0])

        safe = [False] * n
        while queue:
            node = queue.popleft()
            safe[node] = True

            for neighbor in rev_adj_list[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return [node for node in range(n) if safe[node]]


sol = Solution()
print(sol.eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]))
