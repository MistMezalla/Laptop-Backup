#include <bits/stdc++.h>

using namespace std;

vector<int> computeLIS(const vector<int>& A, int n) {
    vector<int> LIS(n, 1);
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (A[i] > A[j]) {
                LIS[i] = max(LIS[i], LIS[j] + 1);
            }
        }
    }
    return LIS;
}

vector<int> computeLDS(const vector<int>& A, int n) {
    vector<int> LDS(n, 1);
    for (int i = n - 2; i >= 0; i--) {
        for (int j = n - 1; j > i; j--) {
            if (A[i] > A[j]) {
                LDS[i] = max(LDS[i], LDS[j] + 1);
            }
        }
    }
    return LDS;
}

int longestBitonicSubsequence(const vector<int>& A, int n) {
    vector<int> LIS = computeLIS(A, n);
    vector<int> LDS = computeLDS(A, n);

    int maxBitonicLength = 0;
    for (int i = 0; i < n; i++) {
        maxBitonicLength = max(maxBitonicLength, LIS[i] + LDS[i] - 1);
    }
    return maxBitonicLength;
}

int main() {
    vector<int> A = {1, 3, 2, 1, 5, 6};
    int n = A.size();
    cout << longestBitonicSubsequence(A, n) << endl;
    return 0;
}
