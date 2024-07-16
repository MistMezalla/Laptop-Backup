'''
-> Usage of list comprehensions.
-> Usage of '_' as throwaway variable(a varia which has no role to play within the body of the loop or
any conditionals)
-> Made smart use of box_ind calc.
'''

class Solution_1(object):
    def isValidSudoku(self, board):
        rows = [[] for _ in range(9)]
        col = [[] for _ in range(9)]
        box = [[] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                box_ind = (i//3)*3 +(j//3)

                if num != ".":
                    if num in rows[i] or num in col[j] or num in box[box_ind]:
                        return False
                    else:
                        rows[i].append(num)
                        col[j].append(num)
                        box[box_ind].append(num)

        return True

sol1 = Solution_1()
print(sol1.isValidSudoku(
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

'''
-> Usage of unique elem property of sets.
-> Very smart use of nested tuples in a list to equate for final len of list and final len of set of list
in order to find any duplicate entries.
'''

class Solution_2(object):
    def isValidSudoku(self, board):
        res = []
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    res += [(i,num),(num,j),(i//3,j//3,num)]

        return len(res) == len(set(res))

sol2 = Solution_2()
print(sol2.isValidSudoku(
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