#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        pair<int,int> find_max_min(vector<int> nums,int p,int r)
        {
            if (p==r)
            {
                return {nums[p],nums[p]};
            }

            int q = (p+r)/2;

            pair<int,int> left = find_max_min(nums,p,q);
            pair<int,int> right = find_max_min(nums,q+1,r);

            return Max_min(left.first,right.first,left.second,right.second);
        }

        pair<int,int> Max_min(int M1,int M2,int m1, int m2)
        {
            int M = M1 >= M2 ? M1 : M2;
            int m = m1 <= m2 ? m1 : m2;

            return {M,m};
        }

    
};

int main()
{
    Solution sol;
    auto res = sol.find_max_min({7,6,3,2,8,10},0,5);
    cout << res.first << endl;
    cout << res.second << endl;
    return 0;
}