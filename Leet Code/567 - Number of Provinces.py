from collections import deque
class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        visited = [0] * len(isConnected)
        queue = deque()
        adj_list = self.adj_list_from_adj_matrix(isConnected)

        i = 0
        curr_number = 0
        while i < len(isConnected):
            if visited[i] != 0:
                i+=1
            else:
                curr_number += 1
                queue.append(i)
                visited[i] = 1

                # adj_matrix based sol
                # while queue:
                #     node = queue.popleft()
                #     for j in range(len(isConnected[node])):
                #         if j != node and isConnected[node][j] != 0:
                #             if not visited[j]:
                #                 visited[j] = 1
                #                 queue.append(j)

                #adj_list based sol
                while queue:
                    node = queue.popleft()

                    for neighbour in adj_list:
                        if not visited[neighbour]:
                            visited[neighbour] = 1
                            queue.append(neighbour)

        return curr_number

    def adj_list_from_adj_matrix(self,matrix):
        adj_list = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]:
                    if i in adj_list:
                        if i != j:
                            adj_list[i].append(j)
                        else:
                            continue
                    else:
                        adj_list[i] = [j]

        return adj_list



sol = Solution()
print(sol.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))
print(sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
print(sol.findCircleNum([
    [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,1,1,1,0,0,0,0,0,0,0,0],
    [0,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1]
]))



