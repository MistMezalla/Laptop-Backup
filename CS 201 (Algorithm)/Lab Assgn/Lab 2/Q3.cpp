#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        int max_product(vector<int> nums,int p,int r)
        {
            if (p==r)
            {
                return nums[p];
            }
            
            int q = (p + r) / 2;
            int left_max = max_product(nums,p,q);
            int right_max = max_product(nums,q+1,r);
            
            int i;
            pair<int,int> left;
            left.first = 1; 
            int curr_product = 1;
            for (i=q;i>-1;i--)
            {
                curr_product *= nums[i];
                left.first = max(left.first,curr_product);
                left.second = min(left.second,curr_product);
                    
            }

            pair<int,int> right;
            right.first = 1;
            curr_product = 1;
            for (i=q+1;i<=r;i++)
            {
                curr_product *= nums[i];
                right.first = max(right.first,curr_product);
                right.second = min(right.second,curr_product);
                       
            }

            return max(max(max(left_max,right_max),left.first * right.first),left.second * right.second);
        }

};

int main()
{
    Solution sol;
    vector<int> arr= {2,3,-1,6,8,0,-2,10,4,-1};
    cout << sol.max_product(arr,0,arr.size() - 1);
    return 0;
}