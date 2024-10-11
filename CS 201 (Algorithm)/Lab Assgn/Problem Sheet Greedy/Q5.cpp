#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        int min_steps(int n)
        {
            if (n==1)
                return 0;

            queue<pair<int,int>> num_step_tracker;
            num_step_tracker.push({1,0});

            set<int> visited;

            while (! num_step_tracker.empty())
            {
                int num = num_step_tracker.front().first;
                int steps = num_step_tracker.front().second;
                num_step_tracker.pop();

                int next_num1 = num + 1;
                if (next_num1 == n)
                    return steps + 1;
                else if (visited.find(next_num1) == visited.end()) // not found condition
                {
                    visited.insert({next_num1,steps+1});
                    num_step_tracker.push({next_num1,steps+1});
                }

                int next_num2 = num * 2;
                if (next_num2 == n)
                    return steps + 1;
                else if (visited.find(next_num2) == visited.end()) 
                {
                    visited.insert({next_num2,steps+1});
                    num_step_tracker.push({next_num2,steps+1});
                }
            }
        }



};

int main()
{
    Solution sol;
    cout<< sol.min_steps(18);
    return 0;
}