#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int MSA_circular(vector<int> &nums) {
        int non_circular_MSA = circular_MSA(nums,0,nums.size() - 1);

        int min_sum = nums[0];
        int total = 0;
        int curr_min = 0;
        for (int i = 0;i<nums.size();i++) {
            curr_min = min(nums[i],nums[i] + curr_min);
            min_sum = min(curr_min,min_sum);
            total += nums[i];
        }

        if (min_sum == total) {
            return non_circular_MSA;
        }
        return max(non_circular_MSA,total - min_sum);
    }

    int circular_MSA(vector<int> &nums,int left,int right) {
        if (left == right)
            return nums[left];

        int mid = (left+right)/2;

        int left_sum = circular_MSA(nums,left,mid);
        int right_sum = circular_MSA(nums,mid+1,right);

        int left_max_suffix = -numeric_limits<float>::infinity(), right_max_prefix = -numeric_limits<float>::infinity();

        int curr_sum = 0;
        for (int i = mid;i > left - 1;i--) {
            curr_sum += nums[i];
            left_max_suffix = max(left_max_suffix,curr_sum);
        }

        curr_sum = 0;
        for (int i = mid + 1;i < right +1 ;i ++) {
            curr_sum += nums[i];
            right_max_prefix = max(right_max_prefix,curr_sum);
        }

        return max({left_sum,right_sum,left_max_suffix,right_max_prefix});
    }


};

int main() {
    Solution sol3;
    vector<int> nums1 = {5, -3, 5, 1};
    vector<int> nums2 ={5, 1, -3, 5};
    vector<int> nums3 = {-3, -2, -3};
    vector<int> nums4  ={-3, 5, 1, -6, 7};
    cout << sol3.MSA_circular(nums1) << endl;  // Example with circular case
    cout << sol3.MSA_circular(nums2) << endl;  // Another circular example
    cout << sol3.MSA_circular(nums3) << endl;   // All negative case
    cout << sol3.MSA_circular(nums4) << endl;  // Mix of positives and negatives
    return 0;

}