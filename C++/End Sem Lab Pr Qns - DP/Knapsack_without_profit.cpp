#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int knapsackWithoutProfitBottomUp(vector<int>& sizes, int limit) {
        vector<vector<int>> memo(limit + 1, vector<int>(sizes.size(), -1));
        for (int i = 0; i <= limit; ++i)
            memo[i][sizes.size() - 1] = (sizes.back() <= i) ? sizes.back() : 0;

        for (int j = sizes.size() - 2; j >= 0; --j) {
            for (int i = 0; i <= limit; ++i) {
                int res1 = 0;
                int res2 = memo[i][j + 1];
                if (i >= sizes[j])
                    res1 = memo[i - sizes[j]][j + 1] + sizes[j];
                memo[i][j] = max(res1, res2);
            }
        }
        return memo[limit][0];
    }

    int knapsackWithoutProfitTopDown(vector<int>& sizes, int limit) {
        vector<vector<int>> memo(limit + 1, vector<int>(sizes.size(), -1));

        function<int(int, int)> rec_helper = [&](int lim, int st) {
            if (st == sizes.size() || lim == 0)
                return 0;
            if (memo[lim][st] != -1)
                return memo[lim][st];

            int res1 = 0, res2 = rec_helper(lim, st + 1);
            if (lim >= sizes[st])
                res1 = rec_helper(lim - sizes[st], st + 1) + sizes[st];

            return memo[lim][st] = max(res1, res2);
        };

        return rec_helper(limit, 0);
    }
};

int main() {
    Solution sol;
    vector<int> sizes = {1, 3, 5, 4};
    int limit = 8;
    cout << sol.knapsackWithoutProfitBottomUp(sizes, limit) << endl;
    cout << sol.knapsackWithoutProfitTopDown(sizes, limit) << endl;
    return 0;
}
