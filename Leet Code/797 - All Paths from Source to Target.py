class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        n = len(graph)
        all_paths = []
        visited = [0]*n

        def dfs(node,path):
            if visited[node]:
                return

            if node == n-1:
                path.append(node)
                all_paths.append(path[:])
                visited[node] = 0
                path.pop()
                return

            visited[node] = 1
            path.append(node)
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    dfs(neighbour,path)
            path.pop()
            visited[node] = 0

        dfs(0,[])
        return all_paths

sol = Solution()
print(sol.allPathsSourceTarget([[1,2],[3],[3],[]]))
print(sol.allPathsSourceTarget(graph = [[4,3,1],[3,2,4],[3],[4],[]]))


