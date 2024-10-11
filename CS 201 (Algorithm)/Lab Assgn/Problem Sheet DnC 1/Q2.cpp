#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        int peakIndexInMountainArray(vector<int>& nums)
        {
            int lo = 0;
            int hi = nums.size() - 1;

            while(hi - lo > 0)
            {
                int mid = (hi+lo)/2;
                if (nums[mid] < nums[mid+1])
                    lo = mid + 1;
                else
                    hi = mid;
            }
            
            return lo;
        }
};

int main()
{
    Solution sol;
    vector<int> nums1 = {10,20,30,98,100,99,98,50};
    vector<int> nums2 = {3,9,8,6,4};
    cout << sol.peakIndexInMountainArray(nums1) << endl;
    cout << sol.peakIndexInMountainArray(nums2) << endl;
    return 0;
}