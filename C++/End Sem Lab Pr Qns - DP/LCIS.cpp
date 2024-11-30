#include <bits/stdc++.h>
using namespace std;

int longestCommonIncreasingSubsequence(vector<int>& A, vector<int>& B) {
    int m = A.size(), n = B.size();
    vector<int> dp(n, 0); // DP array to store the length of LCIS for each element in B

    for (int i = 0; i < m; i++) {
        int prev = 0;  // This stores the value of dp[j-1] before it gets updated
        for (int j = 0; j < n; j++) {
            if (A[i] == B[j]) {
                dp[j] = max(dp[j], prev + 1);
            }
            if (A[i] > B[j]) {
                prev = max(prev, dp[j]);
            }
        }
    }
    return *max_element(dp.begin(), dp.end());
}

int main() {
    vector<int> A = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3};
    vector<int> B = {1, 4, 1, 4, 2, 1, 3, 5, 6, 2, 3, 7, 3, 0, 9, 5};

    cout << "Length of Longest Common Increasing Subsequence: "
         << longestCommonIncreasingSubsequence(A, B) << endl;

    return 0;
}
