'''
Resolved = 1
Revised = 1
'''

'''
-> It is a premium leetcode question
-> Hence solving the spoj qn
'''
from collections import deque
class Solution:
    def __init__(self):
        self.moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
        self.adj_list = {}

    # def coordinates(self,pos: str):
    #     return ord(pos[0]) - ord('a'),ord(pos[1]) - ord('1')

    def isValid_pos(self,pos: str):
        if 'a'<=pos[0]<='h' and '1'<=pos[1]<='8':
            return True
        return False

    def add_edge(self,u,v):
        if u in self.adj_list:
            self.adj_list[u].append(v)
        else:
            self.adj_list[u] = [v]


        # if v in self.adj_list:
        #     self.adj_list[v].append(u)
        # else:
        #     self.adj_list[v] = [u]

    def minKnightMoves(self,source,dest) -> int:
        # x_source,y_source = self.coordinates(source)
        # x_dest,y_dest = self.coordinates(dest)

        level = {key: -1 for key in self.adj_list}
        visited = {key: False for key in self.adj_list}

        queue = deque()
        queue.append(source)
        visited[source] = True
        level[source] = 0
        '''
        -> This test case has failed
        '''
        if source == dest:
            return level[source]

        visited[dest] = False
        level[dest] = -1

        while queue:
            curr = queue.popleft()

            for move in self.moves:
                next = chr(ord(curr[0]) + move[0]) + chr(ord(curr[1]) + move[1])
                if self.isValid_pos(next):
                    self.add_edge(curr,next)
                    visited[next] = False
                    level[next] = -1

            for neighbour in self.adj_list[curr]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)
                    level[neighbour] = level[curr] + 1

            if level[dest] != -1:
                break

        return level[dest]

sol = Solution()
print(sol.minKnightMoves('a1', 'a1'))  # Expected output: 0 #wrong : had given 1
print(sol.minKnightMoves('b1', 'c3'))  # Expected output: 1
print(sol.minKnightMoves('a1', 'c2'))  # Expected output: 1
print(sol.minKnightMoves('a1', 'h8'))  # Expected output: 6
print(sol.minKnightMoves('h8', 'a1'))  # Expected output: 6
print(sol.minKnightMoves('h8', 'c3'))  # Expected output: 4
print(sol.minKnightMoves('b1', 'd2'))  # Expected output: 1
print(sol.minKnightMoves('a1', 'a8'))  # Expected output: 5
print(sol.minKnightMoves('a1', 'h1'))  # Expected output: 5
print(sol.minKnightMoves('d4', 'f7'))  # Expected output: 3
print()

# Additional test cases
print(sol.minKnightMoves('g1', 'h3'))  # Expected output: 1
print(sol.minKnightMoves('a1', 'e5'))  # Expected output: 4
print(sol.minKnightMoves('a1', 'h7'))  # Expected output: 5
print(sol.minKnightMoves('a1', 'g7'))  # Expected output: 4
print(sol.minKnightMoves('d4', 'a8'))  # Expected output: 3
print(sol.minKnightMoves('e5', 'a1'))  # Expected output: 4
print(sol.minKnightMoves('b1', 'g1'))  # Expected output: 3
print(sol.minKnightMoves('a1', 'a7'))  # Expected output: 4














