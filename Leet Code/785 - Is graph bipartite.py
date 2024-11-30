from collections import deque
class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        queue = deque()

        visited = [0]*len(graph)
        lvl = 0
        level = [-1]*len(graph)



        for node in range(len(graph)):
            queue.append(node)
            visited[node] = 1
            while queue:
                n = len(queue)

                for node in queue:
                    level[node] = lvl

                lvl += 1

                for _ in range(n):
                    node = queue.popleft()

                    for neighbour in graph[node]:
                        if level[node] == level[neighbour]:
                            return False
                        if not visited[neighbour]:
                            visited[neighbour] = 1
                            queue.append(neighbour)

        return True

sol = Solution()
print(sol.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))
print(sol.isBipartite([[1,3],[0,2],[1,3],[0,2]]))
print(sol.isBipartite([[3,4],[3,5],[3,4,5],[0,1,2,7],[0,2],[1,2,6],[5,7],[6,3]]))
print(sol.isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]))