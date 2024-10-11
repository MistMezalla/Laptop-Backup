#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    float max_slope(vector<pair<int, int>>& points)
    {
        if (points.size() < 2)
            return numeric_limits<float>::lowest(); //Use numeric_limits<float>::lowest() for negative infinity

        sort(points.begin(), points.end());

        int m = points.size() / 2;
        vector<pair<int, int>> left_half(points.begin(), points.begin() + m);
        vector<pair<int, int>> right_half(points.begin() + m, points.end());

        float left_max = max_slope(left_half);
        float right_max = max_slope(right_half);

        auto min_y_left = *min_element(left_half.begin(), left_half.end(),
                                       [](pair<int, int>& a, pair<int, int>& b) {
                                           return a.second < b.second;
                                       });
        auto max_y_right = *max_element(right_half.begin(), right_half.end(),
                                        [](pair<int, int>& a, pair<int, int>& b) {
                                            return a.second < b.second; // Correct comparison for max y
                                        });

        float cross_slope1 = numeric_limits<float>::lowest(); // Use numeric_limits<float>::lowest()
        if (max_y_right.first != min_y_left.first)
            cross_slope1 = static_cast<float>(max_y_right.second - min_y_left.second) / (max_y_right.first - min_y_left.first);

        // usage of static_cast<float> is just a good coding practice
        // normal float typecasting also serves same purpose
        return max({left_max, right_max, cross_slope1}); // Use initializer list for max
    }
};

int main()
{
    Solution sol;
    vector<pair<int, int>> P = {{1, 3}, {2, 8}, {3, 4}, {4, 10}, {2, 7}, {1, 12}, {5, 6}};
    auto res = sol.max_slope(P);
    cout << res << endl; 
    return 0;
}
