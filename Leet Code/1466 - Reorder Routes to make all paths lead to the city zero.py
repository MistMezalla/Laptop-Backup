class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        cnt = 0

        def dfs(node):
            nonlocal cnt
            visited[node] = 1
            for neighbour,sign in adj_list[node]:
                if not visited[neighbour]:
                    cnt += sign
                    dfs(neighbour)

        adj_list = {key:[] for key in range(n)}
        #parent = {key: None for key in range(n)}
        visited = [0]*n

        for u,v in connections:
            #parent[v] = u
            # if u in adj_list:
            #     adj_list[u].append((v,1))
            #     if v in adj_list:
            #         adj_list[v].append((u,0))
            #     else:
            #         adj_list[v] = [(u,0)]
            # else:
            #     adj_list[u] = [(v,1)]
            #     if v in adj_list:
            #         adj_list[v].append((u,0))
            #     else:
            #         adj_list[v] = [(u,0)]
            adj_list[u].append((v,1))
            adj_list[v].append((u,0))

        dfs(0)
        return cnt

sol = Solution()
print(sol.minReorder(6,[[0,1],[1,3],[2,3],[4,0],[4,5]]))
print(sol.minReorder(8,[[0,1],[1,3],[2,3],[4,0],[4,5],[5,6],[7,6]]))

