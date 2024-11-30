'''
-> A classical question to be solved by union find
    -> though I couldn't think for the same
'''

class Union_Find():
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.rank = [1] * (n+1)

    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
                self.rank[root_x] += self.rank[root_y]
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
                self.rank[root_y] += self.rank[root_x]
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += self.rank[root_y]

            return True

        return False


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        uf = Union_Find(len(edges))
        for u,v in edges:
            if not uf.union(u,v):
                return [u,v]

sol = Solution()
print(sol.findRedundantConnection(edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]))
print(sol.findRedundantConnection(edges = [[1,2],[1,3],[2,3]]))


