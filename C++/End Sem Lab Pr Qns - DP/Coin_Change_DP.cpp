#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int coinChangeBottomUp(vector<int>& coins, int target) {
        vector<int> dp(target + 1, INT_MAX);
        dp[0] = 0;

        for (int coin : coins) {
            for (int i = coin; i <= target; ++i) {
                if (dp[i - coin] != INT_MAX)
                    dp[i] = min(dp[i], dp[i - coin] + 1);
            }
        }

        return dp[target] == INT_MAX ? -1 : dp[target];
    }
};

int main() {
    Solution sol;
    vector<int>coins1 = {1, 6, 4};
    cout << sol.coinChangeBottomUp(coins1, 8) << endl;

    vector<int>coins2 = {1, 3, 4};
    cout << sol.coinChangeBottomUp(coins2, 9) << endl;

    vector<int>coins3 = {2, 4};
    cout << sol.coinChangeBottomUp(coins3, 7) << endl;

    vector<int>coins4 = {3};
    cout << sol.coinChangeBottomUp(coins4, 10) << endl;

    vector<int>coins5 = {5, 10, 5};
    cout << sol.coinChangeBottomUp(coins5, 4) << endl;
    return 0;
}
