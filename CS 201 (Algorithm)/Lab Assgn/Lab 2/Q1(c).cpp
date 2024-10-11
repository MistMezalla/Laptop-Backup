#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        pair<int,int> find_max_2nd_max(vector<int> nums,int p,int r)
        {
            if (p==r)
            {
                return {nums[p],INT_MIN};
            }
            else if (r-p == 1)
            {
                if (nums[r] >= nums[p])
                {
                    return {nums[r],nums[p]};
                }
                else
                    return {nums[p],nums[r]};
            }

            else
            {
                int q = (p+r)/2;

                pair<int,int> left = find_max_2nd_max(nums,p,q);
                pair<int,int> right = find_max_2nd_max(nums,q+1,r);

                return Max_2nd_max(left.first,right.first,left.second,right.second);
            }
        }
        
        pair <int,int> Max_2nd_max(int M1, int M2, int m1, int m2)
        {
            int M,m;
            if (M1 >= M2)
            {
                M = M1;
                m = M2 >= m1 ? M2 : m1;
            }
            else
            {
                M = M2;
                m = M1 >= m2 ? M1 : m2;
            }

            return {M,m};
        }

};

int main()
{
    Solution sol;
    auto res = sol.find_max_2nd_max({7,6,2,8,4,10},0,5);
    cout << res.first << endl;
    cout << res.second << endl;
    return 0;
}