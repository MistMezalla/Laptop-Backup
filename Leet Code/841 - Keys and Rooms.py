class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = [0]*len(rooms)

        def dfs(node):
            if visited[node]:
                return True

            visited[node] = True
            for neighbour in rooms[node]:
                if not visited[neighbour]:
                    dfs(neighbour)

        dfs(0)
        return not any(x == 0 for x in visited)

sol = Solution()
print(sol.canVisitAllRooms([[1],[2],[3],[]]))
print(sol.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))
print(sol.canVisitAllRooms([[1,3,2],[3,0,1],[2],[0]]))
print(sol.canVisitAllRooms([[1,3],[3,0,1,2],[2],[0]]))
        