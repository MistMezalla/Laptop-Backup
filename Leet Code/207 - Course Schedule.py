class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        visited = [0] * numCourses
        arr = [0] * numCourses
        adj_list = {key: [] for key in range(numCourses)}

        for v,u in prerequisites:
            adj_list[u].append(v)
        time = 0
        def dfs(node):
            visited[node] = 1
            nonlocal time
            arr[node] = time
            time += 1
            isTrue = True
            for neighbour in adj_list[node]:
                if not visited[neighbour]:
                    isTrue &= dfs(neighbour)

                elif arr[neighbour] < arr[node]:
                    return False

            return isTrue

        for node in range(numCourses):
            if not visited[node]:
                if not dfs(node):
                    return False

        return True


        