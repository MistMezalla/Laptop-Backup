#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    pair<int, int> find_max_2nd_max(const vector<int> &arr, int p, int r)
    {
        if (p == r) // Only one element
        {
            return {arr[p], INT_MIN}; // INT_MIN represents no second maximum
        }
        else if (r - p == 1) // Two elements
        {
            if (arr[p] >= arr[r])
                return {arr[p], arr[r]};
            else
                return {arr[r], arr[p]};
        }
        else if (r - p >= 2) // More than two elements
        {
            int q = (p + r) / 2;
            pair<int, int> left = find_max_2nd_max(arr, p, q);
            pair<int, int> right = find_max_2nd_max(arr, q + 1, r);
            return max_2nd_max(left.first, right.first, left.second, right.second);
        }
    }

    pair<int, int> max_2nd_max(int M1, int M2, int m1, int m2)
    {
        int M, m;
        
        if (M1 >= M2)
        {
            M = M1;
            m = max(m1, M2);
        }
        else
        {
            M = M2;
            m = max(m2, M1);
        }

        return {M, m};
    }
};

int main()
{
    Solution sol;
    vector<int> nums = {1,7,8,9,2};
    auto result = sol.find_max_2nd_max(nums, 0, nums.size() - 1);
    cout << "Max: " << result.first << endl;
    cout << "2nd Max: " << result.second << endl;
    return 0;
}
