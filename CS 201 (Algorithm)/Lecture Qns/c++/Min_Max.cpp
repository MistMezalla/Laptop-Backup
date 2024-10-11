#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        pair <int,int> find_min_max(const vector<int> &arr)
        {
            int n = arr.size();
            if (n == 0)
                return {INT_MIN,INT_MAX};

            int max_arr,min_arr;
            int i = 0;

            if (n & 1)
            {
                max_arr=min_arr=arr[0];
                i = 1;
            }
            else
            {
                if (arr[0] <= arr[1])
                {
                    max_arr = arr[1];
                    min_arr = arr[0];
                }
                else
                {
                    max_arr = arr[0];
                    min_arr = arr[1];
                }
                i = 2;
            }

            while (i<n-1)
            {
                int curr_min,curr_max;
                if (arr[i]<=arr[i+1])
                {
                    curr_min = arr[i];
                    curr_max = arr[i+1];
                }
                else
                {
                    curr_min = arr[i+1];
                    curr_max = arr[i];
                }

                if (curr_min < min_arr)
                    min_arr = curr_min;

                if (curr_max > max_arr)
                    max_arr = curr_max;
                i+=2;
            }
            return {min_arr,max_arr};
        }
};

int main()
{
    Solution sol;
    vector<int> arr = {8,3,5,6,9,1,10};
    pair<int,int> res = sol.find_min_max(arr);
    cout << res.first << " & " << res.second << endl;
    return 0;
}
