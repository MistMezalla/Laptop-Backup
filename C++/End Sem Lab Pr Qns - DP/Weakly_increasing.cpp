#include <bits/stdc++.h>
using namespace std;

int longestWeaklyIncreasingSubsequence(const vector<int>& A) {
    int n = A.size();
    if (n < 3) return n;

    vector<int> dp(n, 1);

    for (int i = 2; i < n; ++i) {
        for (int j = i - 1; j >= 1; --j) {
            if (2 * A[i] > A[j] + A[j - 1]) {
                dp[i] = max(dp[i], dp[j - 1] + 1);
            }
        }
    }

    return *max_element(dp.begin(), dp.end());
}

int main() {
    vector<int> A = {1, 3, 5, 2, 6, 7, 4};
    cout << longestWeaklyIncreasingSubsequence(A) << endl;
    return 0;
}
