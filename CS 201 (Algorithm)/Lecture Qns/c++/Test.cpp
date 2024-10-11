#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    double closest_pair(vector<pair<int,int>> &points)
    {
        vector<pair<int,int>> points_x = points;
        vector<pair<int,int>> points_y = points;
        sort(points_x.begin(), points_x.end(), [](pair<int,int> &a, pair<int,int> &b)
        {
            return a.first < b.first; // Correct ordering
        });
        sort(points_y.begin(), points_y.end(), [](pair<int,int> &a, pair<int,int> &b)
        {
            return a.second < b.second; // Correct ordering
        });

        return min_dist(points_x, points_y);
    }

    double min_dist(vector<pair<int,int>> &points_x, vector<pair<int,int>> &points_y)
    {
        int n = points_x.size();
        if (n <= 3)
            return brute_force_dist(points_x);

        int m = n / 2;
        pair<int,int> mid_point = points_x[m];

        vector<pair<int,int>> left_x(points_x.begin(), points_x.begin() + m);
        vector<pair<int,int>> right_x(points_x.begin() + m, points_x.end());

        vector<pair<int,int>> left_y, right_y;

        for (auto pt : points_y)
        {
            if (pt.first <= mid_point.first)
                left_y.push_back(pt);
            else
                right_y.push_back(pt);
        }

        double left_min_dist = min_dist(left_x, left_y);
        double right_min_dist = min_dist(right_x, right_y);

        double dist_min = min(left_min_dist, right_min_dist);

        vector<pair<int,int>> strip_pts;
        for (auto pt : points_y)
        {
            if (abs(pt.first - mid_point.first) < dist_min)
                strip_pts.push_back(pt);
        }

        double strip_min_dist = numeric_limits<double>::infinity();
        for (int i = 0; i < strip_pts.size(); ++i)
        {
            for (int j = i + 1; j < min(i + 7, static_cast<int>(strip_pts.size())); ++j)
            {
                if (strip_pts[j].second - strip_pts[i].second >= dist_min)
                    break;
                strip_min_dist = min(strip_min_dist, euclidean_dist(strip_pts[i], strip_pts[j]));
            }
        }

        return min(dist_min, strip_min_dist);
    }

     /*
        -> The reason behind static_cast usage:-
            -> strip_pts.size() returns a size_t, which is an unsigned type. 
            -> Thus to ensure cmp bet int,int in min() static cast is used.
     */

    double brute_force_dist(vector<pair<int,int>> &points)
    {
        double min_dist = numeric_limits<double>::infinity();
        for (int i = 0; i < points.size(); ++i)
        {
            for (int j = i + 1; j < points.size(); ++j)
                min_dist = min(min_dist, euclidean_dist(points[i], points[j]));
        }
        return min_dist;
    }

    double euclidean_dist(pair<int,int> p1, pair<int,int> p2)
    {
        return sqrt(pow(p1.first - p2.first, 2) + pow(p1.second - p2.second, 2));
    }
};

int main()
{
    Solution sol;

    vector<pair<int, int>> points1 = {{2, -5}, {11, -1}, {1, 0}, {12, 8}, {4, 7}, {8, 1}, {10, -4}, {5, 2}, {15, 3}};
    cout << fixed << setprecision(3) << sol.closest_pair(points1) << endl; // Expecting closer to 3.16

    vector<pair<int, int>> points2 = {{1, 1}, {1, 2}, {1, 3}, {1, 4}, {1, 5}, {1, 6}, {1, 7}};
    cout << fixed << setprecision(3) << sol.closest_pair(points2) << endl;

    vector<pair<int, int>> points3 = {{0, 0}, {0, 1}, {1, 0}, {1, 1}, {2, 2}, {3, 3}};
    cout << fixed << setprecision(3) << sol.closest_pair(points3) << endl;

    vector<pair<int, int>> points4 = {{1, 1}, {2, 2}, {3, 3}, {4, 4}, {5, 5}, {6, 6}, {7, 7}, {8, 8}};
    cout << fixed << setprecision(3) << sol.closest_pair(points4) << endl;

    return 0;
}
