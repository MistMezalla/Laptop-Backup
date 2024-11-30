'''
-> Using the concepts of :-
    -> topo sort(Kahn's algo)
    led to errorneous results as you can refer to my code.

-> Few of the errors:-
    -> If simply used Kahn's algo
        -> reported T for nodes bet whom path didn't exist
    -> If tried to do topo sort of individual compo then
        -> missed on the path(forward edges, cross edges and back edges) which were not the part of this algo process
        -> Hence gave F

-> Simple sol:-
    -> Qn is asking to find whether there exists a path bet 2 nodes or not
    -> do bfs/dfs on each node
'''

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        connected = [[False] * numCourses for _ in range(numCourses)]
        adj_list = {key: [] for key in range(numCourses)}

        for u,v in prerequisites:
            adj_list[u].append(v)

        def dfs(node,start):
            for neighbour in adj_list[node]:
                if not connected[start][neighbour]:
                    connected[start][neighbour] = True
                    dfs(neighbour,start)

        for start in range(numCourses):
            dfs(start,start)

        return [connected[u][v] for u,v in queries]
