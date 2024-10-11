#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int maj_elem(vector<int>& nums, int p, int r)
    {
        if (p == r)
        {
            return nums[p];
        }

        int q = (p + r) / 2;

        int left = maj_elem(nums, p, q);
        int right = maj_elem(nums, q + 1, r);

        if (left == right)
        {
            return left;
        }

        int left_count = count(nums.begin() + p, nums.begin() + r + 1, left);
        int right_count = count(nums.begin() + p, nums.begin() + r + 1, right);

        return left_count > right_count ? left : right;
    }
};

int main()
{
    Solution sol;
    vector<int> nums = {2, 2, 1, 1, 1, 2, 2};
    int res = sol.maj_elem(nums, 0, nums.size() - 1);
    cout << "Majority Element: " << res << endl;
    return 0;
}
