#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        int kth_smallest(vector<int>&nums,int k)
        {
            return partition(nums,0,nums.size()-1,k-1);
        }

        int partition(vector<int>&nums,int p,int r,int pos)
        {
            if (p>=r)
                return nums[p];

            int pivot = find_pivot(nums,p,r);
            int left = p;
            int i = p;
            int right = r;

            while (i<=right)
            {
                if (nums[i] < pivot)
                {
                    swap(nums[left],nums[i]);
                    i++;
                    left++;
                }
                else if(nums[i] > pivot)
                {
                    swap(nums[right],nums[i]);
                    right--;
                }
                else
                    i++;
            }

            if (left > pos)
                return partition(nums,p,left,pos);
            else if(right < pos)
                return partition(nums,right,r,pos);
            else
                return nums[pos];
        }

        int find_pivot(vector<int>& nums,int p,int r)
        {
            if (r-p+1<=5)
            {
                sort(nums.begin() + p,nums.begin() + r+1);
                return nums[(p+r)/2];
            }

            vector<int> medians;
            int i;
            for(i=0;i<r+1;i+=5)
            {
                vector<int> part(nums.begin() + i,min(nums.begin() + i+5,nums.begin() + r+1));
                sort(part.begin(),part.end());
                medians.push_back(part[part.size()/2]);
            }

            return find_pivot(medians,0,medians.size()-1);
        }
};

int main()
{
    Solution sol;
    vector<int> nums= {7,2,3,6,10,1,9,4,5,8,19,23,2,7,6,10};
    auto res = sol.kth_smallest(nums,4);
    cout << res;
    return 0;
}