'''
-> Based on arrival times we can't detect the cycles in case of directed graphs
-> we make use of "Kahn's algo" to find "Topo sort" in DAG
    -> It is also used to find cycle in case of directed graphs as well
'''

from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        in_deg = [0] * numCourses
        adj_list = {key:[] for key in range(numCourses)}

        for v,u in prerequisites:
            adj_list[u].append(v)
            in_deg[v] += 1

        queue = deque([node for node in range(numCourses) if in_deg[node] == 0])
        processed_nodes = 0
        while queue:
            node = queue.popleft()
            processed_nodes += 1

            for neighbour in adj_list[node]:
                in_deg[neighbour] -= 1

                if in_deg[neighbour] == 0:
                    queue.append(neighbour)

        if numCourses == processed_nodes:
            return True

        return False
