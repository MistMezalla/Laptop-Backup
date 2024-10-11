#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        pair<int,bool> kth_smallest_elem(vector<int> &nums,int k)
        {
            return partition(nums,0,nums.size()-1,k);
        }
            
        pair<int,bool> partition(vector<int> &nums,int p,int r,int k)
        {
            if (r-p+1 < k)
                return {-1,false};

            int pivot_ind = find(nums.begin() + p, nums.begin()+r+1,find_pivot(nums,p,r)) - nums.begin();
            swap(nums[pivot_ind],nums[r]);

            int x = nums[r];
            int i = p-1;
            int j;
            for (j=p;j<=r-1;j++)
            {
                if (nums[j] <= x)
                {
                    i++;
                    swap(nums[i],nums[j]);
                }
            }
            i++;
            swap(nums[i],nums[r]);

            if (i-p+1==k)
                return {nums[i],true};
            else if(i-p+1>k)
                return partition(nums,p,i,k);
            else
                return partition(nums,i+1,r,k-(i-p+1));
        }

        int find_pivot(vector<int> &nums,int p, int r)
        {
            if (r-p+1 <= 5)
            {
                sort(nums.begin() + p,nums.begin()+r+1);
                return nums[(p+r)/2];
            }

            vector<int> medians;
            int i;
            for (i=p;i<r+1;i+=5)
            {
                int end = min(r+1,i+5);
                sort(nums.begin() + i,nums.begin() + end);
                medians.push_back(nums[i + (end-i)/2]);
            }

            return find_pivot(medians,0,medians.size() - 1);

        }

    

};

int main()
{
    Solution sol;
    vector<int> arr = {3,6,1,4,9,2,8,10,7};
    auto res = sol.kth_smallest_elem(arr,6);
    if (res.second)
        cout << res.first;
    return 0;
}   