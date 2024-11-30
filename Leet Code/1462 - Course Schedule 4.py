from collections import deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[
        bool]:
        adj_list = {key: [] for key in range(numCourses)}
        in_degrees = [0] * numCourses
        visited = [0] * numCourses

        for u,v in prerequisites:
            adj_list[u].append(v)
            in_degrees[v] += 1

        queue = deque([node for node in range(numCourses) if in_degrees[node] == 0])

        def dfs(node,curr_topo):
            visited[node] = 1
            curr_topo.append(node)

            for neighbour in adj_list[node]:
                if not visited[neighbour]:
                    dfs(neighbour,curr_topo)

        comp_topo = []
        while queue:
            start = queue.popleft()
            curr_topo = []
            dfs(start,curr_topo)
            comp_topo.append(curr_topo)

            # topo_sort.append(node)
            #
            # for neighbour in adj_list[node]:
            #     in_degrees[neighbour] -= 1
            #     if in_degrees[neighbour] == 0:
            #         queue.append(neighbour)

        res = []
        pre_query = [[False]*numCourses for _ in range(numCourses)]

        # if not prerequisites:
        #     return [False] * len(queries)

        for topo in comp_topo:
            for i in range(len(topo)):
                for j in range(i+1,len(topo)):
                    u = topo[i]
                    v = topo[j]
                    pre_query[u][v] = True

        for u,v in queries:
            res.append(pre_query[u][v])
        # for i in range(len(topo_sort)):
        #     for j in range(i + 1, len(topo_sort)):
        #         u = topo_sort[i]
        #         v = topo_sort[j]
        #         pre_query[u][v] = True
        #
        #         # Propagate the prerequisites from u to v
        #         for k in range(j + 1, len(topo_sort)):
        #             pre_query[u][topo_sort[k]] = pre_query[u][v]

        return res


sol = Solution()
print(sol.checkIfPrerequisite(numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]))
print(sol.checkIfPrerequisite(numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]))
print(sol.checkIfPrerequisite(numCourses = 2, prerequisites = [[1,0]],queries = [[0,1],[1,0]]))
print(sol.checkIfPrerequisite(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]],queries = [[0,3],[2,0]]))