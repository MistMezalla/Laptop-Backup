#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        int min_cost(vector<int> &files)
        {
            priority_queue<int,vector<int>,greater<int>> min_heap(files.begin(),files.end());

            int res = 0;
            while (min_heap.size() > 1)
            {
                int f1 = min_heap.top();
                min_heap.pop();
                int f2 = min_heap.top();
                min_heap.pop();
                
                min_heap.push(f1 + f2);
                res += f1 + f2;
            }
            
            return res;
        }

};

int main()
{
    Solution sol;
    vector<int> files1 = {4,3,2,6};
    vector<int> files2 = {1,2,3,4,5};
    vector<int> files3 = {10,20,30};
    vector<int> files4 = {5,7,9,12};

    auto res1 = sol.min_cost(files1);
    auto res2 = sol.min_cost(files2);
    auto res3 = sol.min_cost(files3);
    auto res4 = sol.min_cost(files4);

    cout << res1 << " " << res2 << ' ' << res3 << " " << res4;
    return 0;
}