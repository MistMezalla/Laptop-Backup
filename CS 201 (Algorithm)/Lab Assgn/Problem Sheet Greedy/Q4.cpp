#include <bits/stdc++.h>
using namespace std;

/*
-> this solution fails for test case say {{1,2},{1,4},{3,4}};
*/
class Solution_wrong
{
    public:
        int smallest_cover(vector<pair<int,int>> &intervals)
        {
            sort(intervals.begin(),intervals.end());
            vector<pair<int,int>> cover;
            int i = 0;

            while (i < intervals.size())
            {
                int end = intervals[i].second;
                int st = intervals[i].first;
                while (i<intervals.size() && intervals[i].second <= end)
                {
                    i++;
                }
                cover.push_back({st,end});
            }
            return cover.size();
        }

};

class Solution
{
    public:
        int smallest_cover(vector<pair<int,int>> &intervals)
        {
            sort(intervals.begin(),intervals.end());

            vector<pair<int,int>> cover;
            
            int left = -1;
            int right = -1;
            
            for (auto interval: intervals)
            {
                if (interval.first > left && interval.second > right)
                {
                    left = interval.first;
                }
                right = max(right,interval.second);
                if (cover.size() > 0 && interval.first == cover.back().first)
                    cover.pop_back();
                cover.push_back({left,right});
            }

            set<pair<int,int>> cover_set(cover.begin(),cover.end());

            return cover_set.size();
        }
};

int main()
{
    Solution sol;
    vector<pair<int,int>> intervals1 = {{1,3},{2,5},{4,6},{7,8},{6,9}};
    cout << sol.smallest_cover(intervals1) << endl;

    vector<pair<int,int>> intervals2 = {{1,2},{1,4},{3,4}};
    cout << sol.smallest_cover(intervals2) << endl;
 
    return 0;
}