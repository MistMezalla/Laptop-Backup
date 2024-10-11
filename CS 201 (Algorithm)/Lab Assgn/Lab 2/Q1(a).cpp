#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        int max_elem(vector<int> nums,int p, int r)
        {
            if (p == r)
                return nums[p];

            int q = (p+r)/2;
            int max_left = max_elem(nums,p,q);
            int max_right = max_elem(nums,q+1,r);

            return Max_arr(max_left,max_right);
        }

        int Max_arr(int m1, int m2)
        {
            return m1 >= m2 ? m1 : m2;
        }
};

int main()
{
    Solution sol;
    cout << sol.max_elem({5,7,8,1,10,6,4},0,6) << endl;
    return 0;
}