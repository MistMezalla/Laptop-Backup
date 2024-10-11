#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        int find_max(const vector<int> &arr, int p, int r)
        {
            if (p == r)
            {
                return arr[p]; // Base case: return the single element
            }
            else
            {
                int q = (p + r) / 2;
                int max_left = find_max(arr, p, q);
                int max_right = find_max(arr, q + 1, r);
                return Max_arr(max_left, max_right);
            }
        }

        int Max_arr(int m1, int m2)
        {
            return m1 >= m2 ? m1 : m2;
        }
};

int main()
{
    Solution sol;
    vector<int> nums = {9, 5, 7, 3, 4, 6};
    cout << sol.find_max(nums, 0, nums.size() - 1);
    return 0;
}
