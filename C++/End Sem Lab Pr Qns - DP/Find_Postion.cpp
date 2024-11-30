#include <bits/stdc++.h>

using namespace std;

int findPosition(const vector<int>& arr, int x) {
    int low = 0, high = 1;

    while (arr[high] < x) {
        low = high;
        high = 2 * high;
    }

    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == x)
            return mid;
        else if (arr[mid] < x)
            low = mid + 1;
        else
            high = mid - 1;
    }

    return -1;
}

int main() {
    vector<int> arr = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
    int x = 7;

    int result = findPosition(arr, x);
    cout << result << endl;

    return 0;
}
