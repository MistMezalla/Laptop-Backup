class Union_Find():
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[x] > self.rank[y]:
                self.parent[root_y] = root_x
                self.rank[root_x] += self.rank[root_y]

            elif self.rank[x] < self.rank[y]:
                self.parent[root_x] = root_y
                self.rank[root_y] += self.rank[root_x]

            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += self.rank[root_y]

            return True

        return False


class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        uf = Union_Find(n)

        num_edges = 0

        for u,v in connections:
            if uf.union(u,v):
                num_edges += 1

        num_nodes_connected = num_edges + 1
        num_nodes_disconnected = n - num_nodes_connected

        return num_nodes_disconnected if len(connections) - num_edges >= num_nodes_disconnected else -1

sol = Solution()
print(sol.makeConnected(4,[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]]))
