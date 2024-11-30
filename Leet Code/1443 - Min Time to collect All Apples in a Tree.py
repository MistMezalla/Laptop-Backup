class Solution:
    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        cost_node = [0] * n
        parent = {key: None for key in range(n)}
        adj_list = {key: [] for key in range(n)}
        visited = [0] * n

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def dfs(node):
            visited[node] = 1

            for neighbour in adj_list[node]:
                if not visited[neighbour]:
                    parent[neighbour] = node
                    dfs(neighbour)

            if node and (cost_node[node] or hasApple[node]):
                temp = cost_node[node] + 2
                cost_node[parent[node]] += temp


        dfs(0)
        return cost_node[0]

sol = Solution()
print(sol.minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,True,True,False]))
print(sol.minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,False,True,False]))
print(sol.minTime(n = 9, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6],[6,7],[7,8]], hasApple = [False,False,True,False,False,True,False,False,True]))
print(sol.minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,False,True,False]))