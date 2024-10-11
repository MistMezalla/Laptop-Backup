#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        int search(vector<int>& nums ,int val)
        {
            int lo = 0;
            int hi = nums.size() - 1;

            while (hi - lo > 1)
            {
                int mid = (hi + lo)/2;

                if (nums[mid]>val)
                    hi = mid - 1;
                else
                    lo = mid;
            }

            if (nums[lo] == val)
                return lo;
            else if (nums[hi] == val)
                return hi;
            else
                return -1;
        }
};

int main()
{
    Solution sol;
    return 0;
}