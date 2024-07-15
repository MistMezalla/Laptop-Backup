#include <bits/stdc++.h>
using namespace std;

class Solution_2 {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<tuple<int,char,int>> res;
        int i,j;
        for (i=0;i<9;i++)
        {
            for (j=0;j<9;j++)
            {
                char num = board[i][j];
                if (num != '.')
                {
                    res.push_back(make_tuple(i,num,-1));
                    res.push_back(make_tuple(-1,num,j));
                    res.push_back(make_tuple(i/3,num,j/3));
                }
            }
        }
        set<tuple<int,char,int>> s(res.begin(),res.end());
        return res.size() == s.size();
    }
};

class Solution_1 {
    public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<set<int>> rows(9), cols(9), box(9);
        int i,j;
        for (i=0;i<9;i++)
        {
            for (j=0;j<9;j++)
            {
                if (board[i][j] != '.')
                {
                    int box_ind = i/3*3 + j/3;
                    int nums = (board[i][j]) - ('0');
                    if (rows[i].count(nums) || cols[j].count(nums) || box[box_ind].count(nums))
                    {
                        return false;
                    }

                    rows[i].insert(nums);
                    cols[j].insert(nums);
                    box[box_ind].insert(nums);
                }
            }
        }
        return true;
    }
};

int main()
{
    Solution_2 sol;
   vector<vector<char>> board = {
    {'5','3','.','.','7','.','.','.','.'}
,{'6','.','.','1','9','5','.','.','.'}
,{'.','9','8','.','.','.','.','6','.'}
,{'8','.','.','.','6','.','.','.','3'}
,{'4','.','.','8','.','3','.','.','1'}
,{'7','.','.','.','2','.','.','.','6'}
,{'.','6','.','.','.','.','2','8','.'}
,{'.','.','.','4','1','9','.','.','5'}
,{'.','.','.','.','8','.','.','7','9'}};

    cout << sol.isValidSudoku(board);
    return 0;
}