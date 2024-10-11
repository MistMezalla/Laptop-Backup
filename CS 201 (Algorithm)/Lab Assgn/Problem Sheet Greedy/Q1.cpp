#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        int min_intervals(vector<float> &points)
        {
            sort(points.begin(),points.end());

            int intervals = 0;
            int i = 0;
            while (i<points.size())
            {
                float int_end = points[i] + 1;
                intervals ++;

                while (i<points.size() && points[i] <= int_end)
                {
                    i++;
                }
            }
            return intervals;
        }
};

int main()
{
    Solution sol;
    vector<float> points = {0.5,0.7,2.1,1.2,3.9};
    cout << sol.min_intervals(points);
    return 0;
}