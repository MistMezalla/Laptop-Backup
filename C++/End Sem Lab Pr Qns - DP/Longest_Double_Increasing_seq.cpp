#include <bits/stdc++.h>
using namespace std;

int longestDoubleIncreasingSubsequence(const vector<int>& A) {
    int n = A.size();
    if (n < 3) return n;

    vector<int> dp1(n, 1), dp2(n, 1);

    for (int i = 2; i < n; ++i) {
        for (int j = i - 2; j >= 0; --j) {
            if (A[i] > A[j]) {
                dp2[i] = max(dp2[i], dp1[j] + 1);
            }
        }

        for (int j = i - 1; j >= 1; --j) {
            if (A[i] > A[j - 1]) {
                dp1[i] = max(dp1[i], dp2[j - 1] + 1);
            }
        }
    }

    return max(*max_element(dp1.begin(), dp1.end()), *max_element(dp2.begin(), dp2.end()));
}

int main() {
    vector<int> A = {1, 5, 2, 6, 3, 7, 4, 8};
    cout << longestDoubleIncreasingSubsequence(A) << endl;
    return 0;
}
