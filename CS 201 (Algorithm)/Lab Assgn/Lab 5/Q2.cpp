#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        int min_classrooms(vector<pair<int,int>> &classes)
        {
            priority_queue<int,vector<int>,greater<int>> min_heap;

            sort(classes.begin(),classes.end());

            min_heap.push(classes[0].second);

            for (int i = 1;i<classes.size();i++)
            {
                if (classes[i].first >= min_heap.top())
                    min_heap.pop();
                min_heap.push(classes[i].second);

            }
            return min_heap.size();
        }

};

int main()
{
    Solution sol;
    vector<pair<int,int>> classes = {{30,75},{0,50},{60,150}};
    cout << sol.min_classrooms(classes);
    return 0;
}