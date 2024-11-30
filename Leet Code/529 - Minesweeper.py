class Solution:
    def updateBoard(self, board: list[list[str]], click: list[int]) -> list[list[str]]:
        visited = [[0]*len(board[0]) for _ in range(len(board))]

        def isValid(r,c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])

        def dfs(r,c):
            visited[r][c] = 1
            if board[r][c] == "M":
                board[r][c] = "X"
                return


            mines_cnt = 0
            for dx,dy in [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]:
                new_r,new_c = r + dx, c + dy

                if isValid(new_r,new_c) and board[new_r][new_c] == "M":
                    mines_cnt += 1

            if mines_cnt>0:
                board[r][c] = str(mines_cnt)
                return

            board[r][c] = "B"
            for dx,dy in [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]:
                new_r,new_c = r + dx, c + dy

                if isValid(new_r,new_c) and not visited[new_r][new_c]:
                    board[new_r][new_c] = "B"
                    dfs(new_r,new_c)

        dfs(click[0],click[1])
        return board

sol = Solution()
print(sol.updateBoard(board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
                      , click = [3,0]))

print(sol.updateBoard(board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
                      , click = [1,2]))

print(sol.updateBoard(board = [["E","E","M","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
                      , click = [3,0]))

print(sol.updateBoard(board = [["B","2","M","2","B"],["B","2","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
                      , click = [1,2]))



