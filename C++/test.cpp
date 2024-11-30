#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int kth_smallest_sorted_arrays(vector<int>& nums1, vector<int>& nums2, int k) {
        if (nums1.size() > nums2.size())
            return kth_smallest_sorted_arrays(nums2, nums1, k);

        int n1 = nums1.size();
        int n2 = nums2.size();
        int lo = 0, hi = n1;

        while (lo <= hi) {
            int mid1 = lo + (hi - lo) / 2;
            int mid2 = k - mid1;

            int l1 = (mid1 > 0) ? nums1[mid1 - 1] : INT_MIN;
            int l2 = (mid2 > 0) ? nums2[mid2 - 1] : INT_MIN;
            int r1 = (mid1 < n1) ? nums1[mid1] : INT_MAX;
            int r2 = (mid2 < n2) ? nums2[mid2] : INT_MAX;

            if (l1 <= r2 && l2 <= r1) {
                return max(l1, l2);
            } else if (l1 > r2) {
                hi = mid1 - 1;
            } else {
                lo = mid1 + 1;
            }
        }
        return -1; // This line will never be reached due to the problem's constraints
    }
};

int main() {
    Solution sol;
    vector<int> nums1 = {1, 3, 5, 7};
    vector<int> nums2 = {2, 6, 8};
    int res = sol.kth_smallest_sorted_arrays(nums1, nums2, 6);
    cout << res;
    return 0;
}
