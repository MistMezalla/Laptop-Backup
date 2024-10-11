#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        int cnt_inversions(vector<int>&nums,int p,int r)
        {
            if (p>=r)
                return 0;
            
            int q = (p+r)/2;

            int left_cnt = cnt_inversions(nums,p,q);
            int right_cnt = cnt_inversions(nums,q+1,r);

            return left_cnt + right_cnt + Mnc(nums,p,q,r);
        }

        int Mnc(vector<int>&nums,int p,int q,int r)
        {
            int j = q+1;
            int cnt = 0;
            int i;
            for (i = 0;i<nums.size();i++)
            {
                while(j<=r and nums[i] > 2*nums[j])
                    j++;
                cnt += j - (q+1);
            }

            vector<int> res;
            i = p;
            j = q+1;
            while (i<=q && j<=r)
            {
                if (nums[i] > nums[j])
                {
                    res.push_back(nums[j]);
                    j++;
                }
                else
                {
                    res.push_back(nums[i]);
                    i++;
                }
            }

            while (i<=q)
            {
                res.push_back(nums[i]);
                i++;
            }

            while (j<=q)
            {
                res.push_back(nums[j]);
                j++;
            }

            for (i=0;i<res.size();i++)
                nums[p+i] = res[i];

            return cnt;
        }

};

int main()
{
    Solution sol;
    vector<int> nums = {1,3,2,3,1};
    cout << sol.cnt_inversions(nums,0,nums.size()-1);
    return 0;
}