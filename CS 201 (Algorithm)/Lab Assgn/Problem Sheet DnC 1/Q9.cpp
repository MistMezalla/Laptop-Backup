#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        vector<int> pre(nums.size()), suff(nums.size());

        pre[0] = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            pre[i] = nums[i] + max(0, pre[i - 1]);
        }

        suff[nums.size() - 1] = nums[nums.size() - 1];
        for (int i = nums.size() - 2; i >= 0; --i) {
            suff[i] = nums[i] + max(0, suff[i + 1]);
        }

        return MSA(nums, 0, nums.size() - 1, pre, suff);
    }

private:
    int MSA(vector<int>& arr, int left, int right, vector<int>& pre, vector<int>& suff) {
        if (left == right) return arr[left];

        int mid = (left + right) / 2;

        return max({MSA(arr, left, mid, pre, suff), MSA(arr, mid + 1, right, pre, suff), pre[mid] + suff[mid + 1]});
    }
};

int main() {
    Solution sol;
    vector<int> nums1 = {-2,1,-3,4,-1,2,1,-5,4};
    vector<int> nums2 = {1};
    vector<int> nums3 = {5,4,-1,7,8};
    vector<int> nums4 = {-5,-4,-1,-7,-8};

    cout << sol.maxSubArray(nums1) << endl;
    cout << sol.maxSubArray(nums2) << endl;
    cout << sol.maxSubArray(nums3) << endl;
    cout << sol.maxSubArray(nums4) << endl;

    return 0;
}