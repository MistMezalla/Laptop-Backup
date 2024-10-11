#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    pair<int, int> find_min_max(vector<int> &arr, int p, int r)
    {
        if (p == r)
            return {arr[p], arr[p]}; // Base case: single element, min and max are the same
        else
        {
            int q = (p + r) / 2;

            pair<int, int> left = find_min_max(arr, p, q);
            pair<int, int> right = find_min_max(arr, q + 1, r);

            return Max_Min(left.first, right.first, left.second, right.second);
        }
    }

    pair<int, int> Max_Min(int M1, int M2, int m1, int m2)
    {
        int M = M1 >= M2 ? M1 : M2;
        int m = m1 <= m2 ? m1 : m2;
        return {M, m};
    }
};

int main()
{
    Solution sol;
    vector<int> nums = {7, 1, 8, 9, 0, 5, 3, 4};
    auto result = sol.find_min_max(nums, 0, nums.size() - 1);
    cout << "Max: " << result.first << endl;
    cout << "Min: " << result.second << endl;

    return 0;
}
