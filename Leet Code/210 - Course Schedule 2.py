from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        in_degrees = [0] * numCourses
        adj_list = {key:[] for key in range(numCourses)}

        for v,u in prerequisites:
            adj_list[u].append(v)
            in_degrees[v] += 1

        queue =deque([node for node in range(numCourses) if in_degrees[node] == 0])

        topo_sort = []
        while queue:
            node = queue.popleft()
            topo_sort.append(node)

            for neighbour in adj_list[node]:
                in_degrees[neighbour] -= 1
                if in_degrees[neighbour] == 0:
                    queue.append(neighbour)

        return [] if len(topo_sort) != numCourses else topo_sort

sol = Solution()
print(sol.findOrder(numCourses = 2, prerequisites = [[1,0]]))
print(sol.findOrder( numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))
print(sol.findOrder(numCourses = 1, prerequisites = []))



