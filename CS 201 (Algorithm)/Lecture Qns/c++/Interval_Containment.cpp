#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        bool Int_Cont(vector<pair<int,int>> &intervals)
        {
            if (!intervals.size())
                return false;

            sort(intervals.begin(),intervals.end(),[](pair<int,int> a,pair<int,int>b)
            {
                return a.first <= b.first;
            });
            int i;
            int max_end_pt = intervals[0].second;
            for(i=1;i<intervals.size();i++)
            {
                if (intervals[i].second <= max_end_pt)
                    return true;
                
                max_end_pt = intervals[i].second;
            }
            return false;
        }
};

int main()
{
    Solution sol;
    vector<pair<int,int>> intervals = {{1,5},{2,10},{4,12},{7,15}};
    cout << sol.Int_Cont(intervals) << endl;
    return 0;
}