class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # row check
        for i in range(9):
            Set=set(board[i])
            Set.remove('.')
            l = []

            for j in range(9):
                if board[i][j] != ".":
                    l.append(board[i][j])

            if len(Set) != len(l):
                return False

        #column check
        for i in range(9):
            Set=set()
            l = []
            for j in range(9):
                if board[j][i] != ".":
                    Set.add(board[j][i])
                    l.append(board[j][i])

            if len(Set) != len(l):
                return False

        #block check
        d = {}
        for i in range(0,3):
            for j in range(0,3):
               if board[i][j] in d:
                   return False
               else:
                   if board[i][j] != ".":
                       d[board[i][j]] = 1

        d = {}
        for i in range(0, 3):
            for j in range(3,6):
               if board[i][j] in d:
                   return False
               else:
                   if board[i][j] != ".":
                       d[board[i][j]] = 1

        d = {}
        for i in range(0, 3):
            for j in range(6,9):
               if board[i][j] in d:
                   return False
               else:
                   if board[i][j] != ".":
                       d[board[i][j]] = 1

        d = {}
        for i in range(3, 6):
            for j in range(0, 3):
                if board[i][j] in d:
                    return False
                else:
                    if board[i][j] != ".":
                        d[board[i][j]] = 1

        d = {}
        for i in range(3, 6):
            for j in range(3, 6):
                if board[i][j] in d:
                    return False
                else:
                    if board[i][j] != ".":
                        d[board[i][j]] = 1

        d = {}
        for i in range(3, 6):
            for j in range(6, 9):
                if board[i][j] in d:
                    return False
                else:
                    if board[i][j] != ".":
                        d[board[i][j]] = 1

        d = {}
        for i in range(6, 9):
            for j in range(0, 3):
                if board[i][j] in d:
                    return False
                else:
                    if board[i][j] != ".":
                        d[board[i][j]] = 1

        d = {}
        for i in range(6, 9):
            for j in range(3, 6):
                if board[i][j] in d:
                    return False
                else:
                    if board[i][j] != ".":
                        d[board[i][j]] = 1

        d = {}
        for i in range(6, 9):
            for j in range(6, 9):
                if board[i][j] in d:
                    return False
                else:
                    if board[i][j] != ".":
                        d[board[i][j]] = 1
        return True

my_sol = Solution()
print(my_sol.isValidSudoku(
[[".",".",".",".","5",".",".","1","."],
 [".","4",".","3",".",".",".",".","."],
 [".",".",".",".",".","3",".",".","1"],
 ["8",".",".",".",".",".",".","2","."],
 [".",".","2",".","7",".",".",".","."],
 [".","1","5",".",".",".",".",".","."],
 [".",".",".",".",".","2",".",".","."],
 [".","2",".","9",".",".",".",".","."],
 [".",".","4",".",".",".",".",".","."]]
))

