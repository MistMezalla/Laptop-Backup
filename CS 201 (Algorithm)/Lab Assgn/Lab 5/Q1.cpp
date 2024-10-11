#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        vector<pair<int,int>> max_non_overlapping_classes(vector<pair<int,int>> &intervals)
        {
            sort(intervals.begin(),intervals.end(),[](pair<int,int> &a, pair<int,int> &b)
            {
                return a.second <= b.second;
            });

            vector<pair<int,int>> res;
            int end_time = numeric_limits<int>::infinity();
            for(auto interval: intervals)
            {
                if (interval.first > end_time)
                {
                    res.push_back(interval);
                    end_time = res.back().second;
                }
            }

            return res;
        }

};

int main()
{
    Solution sol;
    vector<pair<int,int>> intervals = {{0, 3}, {2, 4}, {3, 5}, {1, 6}, {5, 7}, {6, 8}, {8, 9}};
    auto res = sol.max_non_overlapping_classes(intervals);
    for (auto item: res)
    {
        cout << item.first << "," << item.second << endl;
    }

    return 0;
}