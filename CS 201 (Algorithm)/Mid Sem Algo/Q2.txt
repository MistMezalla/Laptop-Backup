#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int max_subarray(vector<int> & nums) {
        auto res = MSA_DnC(nums,0,nums.size()- 1);
        return res.first;
    }

    pair<int,int> MSA_DnC(vector<int> &nums,int left,int right) {
        if (left >= right) {
            if (nums[left] < 0)
                return {nums[left],nums[left]};
            else
                return {nums[left],0};
        }


        int mid = (left + right) / 2;

        pair<int,int> left_MSA = MSA_DnC(nums,left,mid);
        pair<int,int> right_MSA = MSA_DnC(nums,mid + 1,right);

        int left_sum = 0, right_sum = 0,curr_sum = 0;

        int tbd_left = INT_MAX;
        for (int i = mid - 1;i >left - 1;i--) {
            if (nums[i] < 0)
                tbd_left = min(tbd_left,nums[i]);
            curr_sum += nums[i];
            left_sum = max(left_sum,curr_sum);
        }

        curr_sum = 0;
        int tbd_right = INT_MAX;
        for (int i = mid + 1; i < right + 1; i++) {
            if (nums[i] < 0)
                tbd_right = min(tbd_left,nums[i]);
            curr_sum += nums[i];
            right_sum = max(right_sum, curr_sum);
        }

        int tbd_cross = min(tbd_left,tbd_right);
        pair<int,int> cross_MSA = {left_sum + nums[mid] + right_sum,tbd_cross};

        return {max({left_MSA.first,right_MSA.first,cross_MSA.first}),min({left_MSA.second,right_MSA.second,cross_MSA.second})};
        //return max({MSA_DnC(nums,left,mid-1),MSA_DnC(nums,mid+1,right),left_sum + nums[mid] + right_sum});
    }
};

int main() {
    Solution sol;
    vector<int> nums1 = {1,-2,0,3};
    vector<int> nums2 = {-1,-1,-2,-3};
    vector<int> nums3 = {1, 2, 3, -2, 5};

    cout << sol.max_subarray(nums1) << endl;
    cout << sol.max_subarray(nums2) << endl;
    cout << sol.max_subarray(nums3) << endl;
    return 0;
}