class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        visited = [0] * n
        adj_list = {key: [] for key in range(n)}
        comp_number = 1

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def dfs(node,n,m):
            visited[node] = comp_number
            n[0] += 1

            for neighbour in adj_list[node]:
                m[0] +=1
                if not visited[neighbour]:
                    dfs(neighbour,n,m)


        cnt = 0
        for node in range(n):
            num_nodes = [0]
            num_edges = [0]
            if not visited[node]:
                dfs(node,num_nodes,num_edges) # num nodes and sum of degress
                num_edges[0] //= 2

                if num_edges[0] == (num_nodes[0]) * (num_nodes[0] - 1) // 2:
                    cnt += 1

                comp_number += 1

        return cnt

sol = Solution()
print(sol.countCompleteComponents(n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]))
print(sol.countCompleteComponents(n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]))
print(sol.countCompleteComponents(11,[[0,1],[1,2],[3,4],[4,5],[5,3],[6,7],[7,8],[8,9],[7,9],[6,8]]))

