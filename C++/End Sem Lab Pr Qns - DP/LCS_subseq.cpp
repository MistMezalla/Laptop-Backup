#include <bits/stdc++.h>
using namespace std;

int longestCommonSubsequence(string s1, string s2) {
    int m = s1.size(), n = s2.size();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (s1[i - 1] == s2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    return dp[m][n];
}

int main() {
    string s1 = "secret", s2 = "secretary";
    cout << longestCommonSubsequence(s1, s2) << endl;  // Output: 6
    s1 = "bisect", s2 = "trisect";
    cout << longestCommonSubsequence(s1, s2) << endl;  // Output: 5
    s1 = "bisect", s2 = "secret";
    cout << longestCommonSubsequence(s1, s2) << endl;  // Output: 4
    s1 = "director", s2 = "secretary";
    cout << longestCommonSubsequence(s1, s2) << endl;  // Output: 4
    return 0;
}
