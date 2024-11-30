#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minCost(vector<vector<int>>& grid) {
        int m = static_cast<int>(grid.size());
        int n = static_cast<int>(grid[0].size());

        vector<vector<int>> cost (m,vector<int>(n,INT_MAX));
        vector<pair<int,int>> dir = {{0,1},{0,-1},{1,0},{-1,0}};
        cost[0][0] = 0;
        deque<tuple<int,int,int>> dq; // cost,r,c
        dq.emplace_back(0,0,0);

        while (!dq.empty()) {
            int curr_cost,r,c;
            tie(curr_cost,r,c) = dq.front();
            dq.pop_front();

            for (int ind = 0;ind < 4;ind++) {
                int new_r = dir[ind].first + r;
                int new_c = dir[ind].second + c;

                if (isValid(new_r,new_c,m,n)) {
                    int new_cost = grid[r][c] == ind + 1 ? curr_cost : curr_cost + 1;

                    if (new_cost < cost[new_r][new_c]) {
                        cost[new_r][new_c] = new_cost;
                        if (grid[r][c] == ind + 1) {
                            dq.emplace_front(curr_cost,new_r,new_c);
                        }
                        else {
                            dq.emplace_back(curr_cost + 1,new_r,new_c);
                        }
                    }

                }

            }
        }
        return cost[m-1][n-1];
    }

    bool isValid(int r,int c,int m,int n) {
        return 0 <= r && r < m && 0 <= c && c < n;
    }
};

int main() {
    Solution sol;
    vector<vector<int>> grid = {{1, 1, 3}, {4, 3, 2}};
    cout << sol.minCost(grid) << endl;  // Output: 1
    return 0;
}