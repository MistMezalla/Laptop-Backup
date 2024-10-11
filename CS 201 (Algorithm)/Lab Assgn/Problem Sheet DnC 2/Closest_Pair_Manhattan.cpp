#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        double closest_pair_manhattan(vector<pair<int,int>>& points)
        {
            vector<pair<int,int>> points_x = points;
            vector<pair<int,int>> points_y = points;

            sort(points_x.begin(),points_x.end(),[](pair<int,int> a,pair<int,int> b)
            {
                return a.first <= b.first;
            });

            sort(points_y.begin(),points_y.end(),[](pair<int,int> a,pair<int,int> b)
            {
                return a.second <= b.second;
            });

            return min_dist(points_x,points_y);
        }

        double min_dist(vector<pair<int,int>> &points_x, vector<pair<int,int>> &points_y)
        {
            int n = points_x.size();
            if (n <= 3)
                return brute_force(points_x);
        }

        double brute_force(vector<pair<int,int>> &points)
        {
            double minimum_dist = numeric_limits<double>::infinity();
            int i,j;
            for (i = 0;i<points.size();i++)
            {
                for (j = i+1;j<points.size();j++)
                    minimum_dist = min(minimum_dist,manhattan_dist(points[i],points[j]));
            }
        }

};

int main()
{

    return 0;
}