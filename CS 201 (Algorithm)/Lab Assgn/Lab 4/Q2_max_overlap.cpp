#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        int max_length(vector<pair<int,int>> &points)
        {
            sort(points.begin(),points.end());

            pair<int,int> max_interval = points[0];
            int max_overlap_length = - numeric_limits<int>::infinity();
            int i;
            for (i=1;i<points.size();i++)
            {
                if (points[i].first >= max_interval.first && points[i].second <= max_interval.second)
                    max_interval = points[i];
                
                int min_pt = max(points[i].first, max_interval.first);
                int max_pt = min(points[i].second, max_interval.second);

                max_overlap_length = max(max_overlap_length,max_pt - min_pt + 1);

            }

            return max_overlap_length;
    }

};

int main()
{
    Solution sol;
    vector<pair<int,int>>points = {{3,5},{1,7},{2,8},{5,10},{6,9}};
    auto res = sol.max_length(points);
    cout << res;
    return 0;
}