#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int cnt_inversions(vector<int> &nums, int p, int r)
    {
        if (p >= r)
            return 0;

        int q = (p + r) / 2;
        int left_cnt = cnt_inversions(nums, p, q);
        int right_cnt = cnt_inversions(nums, q + 1, r);

        return left_cnt + right_cnt + MnC(nums, p, q, r);
    }

    int MnC(vector<int> &nums, int p, int q, int r)
    {
        int i = p;
        int j = q + 1;
        vector<int> res;
        int cnt = 0;

        while (i <= q && j <= r)
        {
            if (nums[j] < nums[i])
            {
                res.push_back(nums[j]);
                j++;
                cnt += (q - i + 1);
            }
            else
            {
                res.push_back(nums[i]);
                i++;
            }
        }

        while (i <= q)
        {
            res.push_back(nums[i]);
            i++;
        }

        while (j <= r)
        {
            res.push_back(nums[j]);
            j++;
        }

        for (i = 0; i < res.size(); i++)
            nums[p + i] = res[i];

        return cnt;
    }
};

int main()
{
    Solution sol;
    
    vector<int> arr1 = {1, 3, 5, 4, 2};
    cout << sol.cnt_inversions(arr1, 0, arr1.size() - 1) << endl;

    vector<int> arr2 = {1, 2, 3, 4, 5};
    cout << sol.cnt_inversions(arr2, 0, arr2.size() - 1) << endl;

    vector<int> arr3 = {5, 4, 3, 2, 1};
    cout << sol.cnt_inversions(arr3, 0, arr3.size() - 1) << endl;

    vector<int> arr4 = {2, 2, 2, 2, 2};
    cout << sol.cnt_inversions(arr4, 0, arr4.size() - 1) << endl;

    vector<int> arr5 = {1, 3, 2, 4, 5};
    cout << sol.cnt_inversions(arr5, 0, arr5.size() - 1) << endl;

    vector<int> arr6 = {8, 4, 2, 1};
    cout << sol.cnt_inversions(arr6, 0, arr6.size() - 1) << endl;

    return 0;
}
