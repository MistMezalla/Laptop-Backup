#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        vector<int> kth_smallest_elem_2_sorted_arays(vector<int>& nums1,vector<int>& nums2,int k)
        {
            int lo = min(nums1[0],nums2[0]);
            int hi = max(nums1.back(),nums2.back());

            while (hi - lo > 1)
            {
                int mid = (hi+lo)/2;

                int cnt1 = elem_less(nums1,mid);
                int cnt2 = elem_less(nums2,mid);

                if (cnt1 + cnt2 < k)
                    lo = mid + 1;
                else    
                    hi = mid;
            }

            int kth_lowest;
            if (elem_less(nums1,lo) + elem_less(nums2,lo) == k)
                kth_lowest = lo;
            else
                kth_lowest = hi;

            int cnt1 = elem_less(nums1,kth_lowest);
            int cnt2 = elem_less(nums2,kth_lowest);

            vector<int> res;
            int i,j;
            i = j =0;

            while (res.size() < k)
            {
                if (i<cnt1 and (j==cnt2 or nums1[i]<=nums2[j]))
                {
                    res.push_back(nums1[i]);
                    i++;
                }
                else
                {
                    res.push_back(nums2[j]);
                    j++;
                }        
            }
            return res;
        }

        int elem_less(vector<int>&nums,int val)
        {
            int lo = 0;
            int hi = nums.size();

            while (hi - lo > 1)
            {
                int mid = (hi+lo)/2;
                if (nums[mid] <=val)
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
    vector<int> nums1 = {1,3,5,7};
    vector<int> nums2 = {2,8};
    auto res = sol.kth_smallest_elem_2_sorted_arays(nums1,nums2,5);
    for (auto num: res)
        cout << num << ' ';
    return 0;
}