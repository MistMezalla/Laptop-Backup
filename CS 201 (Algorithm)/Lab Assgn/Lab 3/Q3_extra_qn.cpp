#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        int kth_smallest_sorted_arrays(vector<int>& nums1,vector<int>& nums2,int k)
        {
            if (nums1.size() > nums2.size())
                return kth_smallest_sorted_arrays(nums2,nums1,k);
            
            int lo = 0;
            int hi = nums1.size();

            while (hi - lo > -1)
            {
                int mid1 = (hi + lo)/2;
                int mid2 = k - mid1;
                // mid1 + mid2 => Total k elem chosen from two arrays altogether

                // Handling the cases where mid2 is going out of bound
                // i.e, left part is too small or too large
                if (mid2 < 0)
                {
                    hi = mid1 - 1;
                    continue;
                }
                else if (mid2 > nums2.size())
                {
                    lo = mid1 + 1;
                    continue;
                }
                    
                int l1 = mid1>0 ? nums1[mid1-1] : INT_MIN;
                int l2 = mid2>0 ? nums2[mid2 - 1] : INT_MIN;
                int r1 = mid1 < nums1.size() ? nums1[mid1] : INT_MAX;
                int r2 = mid2 < nums2.size() ? nums2[mid2] : INT_MAX;


                if (l1 <= r2 && l2 <= r1)
                    return max(l1,l2);
                else if (l1 > r2)
                    hi = mid1 - 1;
                else
                    lo = mid1 + 1;
            }
            
        }

};

int main()
{
    Solution sol;
    vector<int> nums1 = {-3,-2,-1,-1,1,3,3,5,5,7};
    vector<int> nums2 = {2,6,6,8};
    auto res = sol.kth_smallest_sorted_arrays(nums1,nums2,10);
    cout << res;
    return 0;
}