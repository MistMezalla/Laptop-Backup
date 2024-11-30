from typing import List
from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n == 1:
            return True

        # adj_matrix = [[0]*n for _ in range(n)]
        #
        # for u,v in edges:
        #     adj_matrix[u][v] = 1
        #     adj_matrix[v][u] = 1
        adj_list = {}

        for u,v in edges:
            if u in adj_list:
                adj_list[u].append(v)
            else:
                adj_list[u] = [v]

            if v in adj_list:
                adj_list[v].append(u)
            else:
                adj_list[v] = [u]


        queue = deque()
        queue.append(source)
        visited = [0] * n
        visited[source] = 1

        while queue:
            node = queue.popleft()

            # for i in range(n):
            #     if adj_matrix[node][i] == 1 and not visited[i]:
            #         if i == destination:
            #             return True
            #         queue.append(i)
            #         visited[i] = 1
            if node not in adj_list:
                adj_list[node] = []

            for neighbour in adj_list[node]:
                if neighbour == destination:
                    return True

                if not visited[neighbour]:
                    visited[neighbour] = 1
                    queue.append(neighbour)

        return False

def test_valid_path():
    # Example test case
    n = 10
    edges = [[4,5],[4,7],[7,8],[7,6],[1,3],[2,3] ]
    source = 4
    destination = 6

    # Create solution instance and test
    solution = Solution()
    result = solution.validPath(n, edges, source, destination)
    print(f"Path exists from {source} to {destination}: {result}")

# Run the test function
test_valid_path()

