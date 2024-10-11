#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        int max_non_overlapping_arcs(vector<pair<int,int>> &arcs)
        {
            sort(arcs.begin(),arcs.end());

            vector<pair<int,int>> non_overlapping_arcs;

            int end = -numeric_limits<int>::infinity();
            for(auto arc: arcs)
            {
                if (arc.first >= end)
                {
                    end = arc.second;
                    non_overlapping_arcs.push_back(arc);
                }
            }
            return non_overlapping_arcs.size();
        }

};

int main()
{
    Solution sol;
    vector<pair<int,int>> arcs = {{30, 60}, {45, 90}, {90, 180}, {170, 270}, {200, 240}};
    cout<< sol.max_non_overlapping_arcs(arcs);
    return 0;
}