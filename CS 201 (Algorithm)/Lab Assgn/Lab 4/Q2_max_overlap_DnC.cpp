#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        int max_overlap_length(vector<pair<int,int>> &points)
        {
            sort(points.begin(),points.end());
            return max_overlap(points);
        }
        int max_overlap(vector<pair<int,int>> &points)
        {
            if (points.size() <= 2)
            {
                if (points.size() == 2 && points[0].second >= points[1].first)
                    return min(points[0].second, points[1].second) - max(points[0].first,points[1].first) + 1;
                
                else
                    return 0;
            }

            int m = points.size()/2;
            vector<pair<int,int>> left_half(points.begin(),points.begin() + m);
            vector<pair<int,int>> right_half(points.begin() + m,points.end());

            int left_overlap = max_overlap(left_half);
            int right_overlap = max_overlap(right_half);

            pair<int,int> left_max_cross_interval = *max_element(left_half.begin(),left_half.end(),[](pair<int,int> &a,pair<int,int> &b)
            {
                return a.second <= b.second;
            });

            return max(max(left_overlap, right_overlap ), cross_overlap(left_max_cross_interval,right_half));
        }

        int cross_overlap(pair<int,int> &left_cross,vector<pair<int,int>> &right_half)
        {
            int cross_dist = - numeric_limits<int>::infinity();
            for (auto pt: right_half)
            {
                if (left_cross.second >= pt.first)
                {
                    cross_dist = max(cross_dist,min(left_cross.second,pt.second) - pt.first + 1);
                }
            }

            return cross_dist;
        }

};

int main()
{
    Solution sol;
    vector<pair<int,int>>points = {{3,5},{1,7},{2,8},{5,10},{6,9}};
    auto res = sol.max_overlap_length(points);
    cout << res;
    return 0;
}