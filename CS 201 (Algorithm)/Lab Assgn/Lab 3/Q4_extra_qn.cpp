#include <bits/stdc++.h>
using namespace std;
//This code assumes that len of each arr is 'atleast 1' and k is >= 3.
class Solution
{
    public:
        int kth_smallest_sorted_arrays(vector<int> nums1,vector<int> nums2,vector<int> nums3,int k)
        {
            int lo = min(min(nums1[0],nums2[0]),nums3[0]);
            int hi = max(max(nums1.back(),nums2.back()),nums3.back());

            while (hi - lo > 1)
            {
                int mid = (hi+lo)/2;

                int cnt1 = elem_less(nums1,mid);
                int cnt2 = elem_less(nums2,mid);
                int cnt3 = elem_less(nums3,mid);

                if (cnt1 + cnt2 + cnt3 < k)
                    lo = mid + 1 ;
                else
                    hi = mid;
            }

            if (elem_less(nums1,lo) + elem_less(nums2,lo) + elem_less(nums3,lo) == k)
                return lo;
            return hi;

        }

        int elem_less(vector<int>&nums,int val)
        {
            int lo = 0;
            int hi = nums.size();

            while (hi - lo > 1)
            {
                int mid = (hi + lo)/2;
                
                if (nums[mid] <= val)
                    lo = mid + 1;
                else
                    hi = mid;
            }
            if (nums[lo] > val)
                return lo;
            return hi;
        }

};

int main()
{
    Solution sol;
    vector<int> nums1 = {1};
    vector<int> nums2 = {2};
    vector<int> nums3 = {4};
    auto res = sol.kth_smallest_sorted_arrays(nums1,nums2,nums3,2);
    cout << res;
    return 0;
}