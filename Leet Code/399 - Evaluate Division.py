from collections import deque
class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        adj_list = {}

        for ind,(u,v) in enumerate(equations):
            if u not in adj_list:
                adj_list[u] = [(v,values[ind])]
            else:
                adj_list[u].append((v,values[ind]))

            if v not in adj_list:
                adj_list[v] = [(u, 1/values[ind])]
            else:
                adj_list[v].append((u, 1/values[ind]))


        #solution = {key: {key: 1 for key in adj_list} for key in adj_list}
        #visited = {key: 0 for key in adj_list}
        def bfs(start,end):
            visited = set()
            queue = deque([(start,1.000)])
            while queue:
                node,curr_product = queue.popleft()
                visited.add(node)
                if node == end:
                    return curr_product

                for neighbour,wt in adj_list[node]:
                    if neighbour not in visited:
                        queue.append((neighbour,curr_product * wt))
            return -1.00

        # node_list = list(adj_list.keys())
        # start = node_list[0]
        # dfs(start,start)

        res = []
        for u,v in queries:
            if u not in adj_list:
                res.append(-1.000)
            else:
                res.append(bfs(u,v))


        return res

sol = Solution()
print(sol.calcEquation([["a","b"],["c","d"]],[1.0,1.0],[["a","c"],["b","d"],["b","a"],["d","c"]]))
print(sol.calcEquation([["a","b"]],[0.5],[["a","b"],["b","a"],["a","c"],["x","y"]]))


