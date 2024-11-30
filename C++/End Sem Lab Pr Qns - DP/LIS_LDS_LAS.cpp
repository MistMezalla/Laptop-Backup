#include <bits/stdc++.h>
using namespace std;

int LIS(vector<int>& arr) {
    vector<int> dp(arr.size(), 1);
    for (int i = 1; i < arr.size(); i++) {
        for (int j = 0; j < i; j++) {
            if (arr[i] > arr[j]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }
    return *max_element(dp.begin(), dp.end());
}

int LDS(vector<int>& arr) {
    vector<int> dp(arr.size(), 1);
    for (int i = 1; i < arr.size(); i++) {
        for (int j = 0; j < i; j++) {
            if (arr[i] < arr[j]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }
    return *max_element(dp.begin(), dp.end());
}

int LAS(vector<int>& arr) {
    if (arr.size() == 0) return 0;
    vector<int> inc(arr.size(), 1), dec(arr.size(), 1);
    for (int i = 1; i < arr.size(); i++) {
        for (int j = 0; j < i; j++) {
            if (arr[i] > arr[j]) {
                inc[i] = max(inc[i], dec[j] + 1);
            }
            if (arr[i] < arr[j]) {
                dec[i] = max(dec[i], inc[j] + 1);
            }
        }
    }
    return max(*max_element(inc.begin(), inc.end()), *max_element(dec.begin(), dec.end()));
}

int main() {
    vector<int> arr = {1, 3, 2, 4, 5};
    cout << "LIS: " << LIS(arr) << endl;
    cout << "LDS: " << LDS(arr) << endl;
    cout << "LAS: " << LAS(arr) << endl;
    return 0;
}
