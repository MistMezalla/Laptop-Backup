#include <bits/stdc++.h>
using namespace std;

int shortestOscillatingSupersequence(const vector<int>& A) {
    int n = A.size();
    if (n == 0) return 0;

    vector<int> up(n, 1), down(n, 1);

    for (int i = 1; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (A[i] > A[j]) {
                up[i] = min(up[i], down[j] + 1);
            } else if (A[i] < A[j]) {
                down[i] = min(down[i], up[j] + 1);
            }
        }
    }

    return min(up[n-1], down[n-1]);
}

int main() {
    vector<int> A = {1, 7, 4, 9, 2, 5};
    cout << shortestOscillatingSupersequence(A) << endl;
    return 0;
}
