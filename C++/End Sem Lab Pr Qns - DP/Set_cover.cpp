#include <bits/stdc++.h>
using namespace std;

vector<set<int>> F;
set<int> U;

int OPT(int i, set<int> A) {
    if (A.empty()) return 0;
    if (i >= F.size()) return INT_MAX;

    int res = OPT(i + 1, A);

    set<int> newA = A;
    newA.erase(F[i].begin(), F[i].end());

    res = min(res, OPT(i + 1, newA) + 1);

    return res;
}

int main() {
    U = {1, 2, 3, 4, 5};

    F.push_back({1, 2, 3});
    F.push_back({2, 3});
    F.push_back({4, 5});
    F.push_back({1, 2, 4});

    set<int> A = U;

    cout << "Minimum number of sets required to cover U: " << OPT(0, A) << endl;

    return 0;
}
