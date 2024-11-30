# include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int regionsBySlashes(vector<string>& grid) {
        int n = grid.size();
        vector<vector<string>> exp_grid(3*n,vector<string>(3*n,"0"));

        int i,j;
        for (i = 0;i < n;i++) {
            for (j = 0;j < n ;j++) {
                int r = 3 * i;
                int c = 3 * j;

                if (grid[i][j] == '\\') {
                    exp_grid[r][c] = "1";
                    exp_grid[r+1][c+1] = "1";
                    exp_grid[r+2][c+2] = "1";
                }
                else if (grid[i][j] == '/') {
                    exp_grid[r][c+2] = "1";
                    exp_grid[r+1][c+1] = "1";
                    exp_grid[r+2][c] = "1";
                }
            }
        }

        vector<vector<int>> visited (3*n,vector<int>(3*n,0));

        int r,c;
        int cnt = 0;
        for (r = 0;r<3*n;r++) {
            for (c= 0;c < 3 * n ;c++) {
                if (exp_grid[r][c] == "0" and ! visited[r][c]) {
                    dfs(r,c,visited,exp_grid);
                    cnt ++;
                }
            }
        }

        return cnt;
    }

    void dfs(int r,int c,vector<vector<int>> &visited,vector<vector<string>> & exp_grid) {
        visited[r][c] = 1;

        vector<pair<int,int>> dir = {{-1,0},{1,0},{0,1},{0,-1}};

        for (auto direction: dir) {
            int new_r = r + direction.first;
            int new_c = c + direction.second;

            if (isValid(new_r,new_c,static_cast<int>(visited.size())) && exp_grid[new_r][new_c] == "0" && ! visited[new_r][new_c]) {
                dfs(new_r,new_c,visited,exp_grid);
            }
        }
    }

    bool isValid(int r,int c,int n) {
        return 0 <= r && r < n && 0 <= c && c < n;
    }
};

int main() {
    Solution sol;

    vector<string> grid1 = {" /","  "};
    cout << sol.regionsBySlashes(grid1);
}