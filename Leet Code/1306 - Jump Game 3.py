class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        visited = [0] * len(arr)

        def isValid(ind):
            return 0 <= ind < len(arr)

        def dfs(node):
            if visited[node]:
                return False

            visited[node] = 1
            if_zero = False
            if isValid(node + arr[node]):
                if arr[node + arr[node]] == 0:
                    return True
                if not visited[node + arr[node]]:
                    if_zero |= dfs(node + arr[node])

            if isValid(node - arr[node]):
                if arr[node - arr[node]] == 0:
                    return True

                if not visited[node - arr[node]]:
                    if_zero |= dfs(node - arr[node])

            return if_zero

        return dfs(start)

sol = Solution()
print(sol.canReach(arr = [3,1,2,0,3,1,2], start = 5))
print(sol.canReach([2,2,3,2,3],3))
