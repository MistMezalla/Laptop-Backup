#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        int missing_number(vector<int> nums,int lo, int hi)
        {
            while (hi - lo > 1)
            {
                int mid = (hi + lo) / 2;

                if (nums[mid] - mid != nums[lo] - lo)
                {
                    hi = mid;
                }
                else
                    lo = mid;
            }

            return nums[lo] + 1;

        }
};

int main()
{
    Solution sol;
    cout << sol.missing_number({1,2,3,4,5,7,8},0,6);
    return 0;
}