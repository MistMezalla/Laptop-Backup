#include <bits/stdc++.h>
using namespace std;

class Solution1
{
    public:
        int min_time_single_sys(vector<pair<string,int>> &jobs)
        {
            sort(jobs.begin(),jobs.end(),[](pair<string,int> &a, pair<string,int> &b)
            {
                return a.second <= b.second;
            });

            int tot_time = 0;
            int curr_time = 0;

            for(auto job: jobs)
            {
                curr_time += job.second;
                tot_time += curr_time;
            }

            return tot_time;
        }
};


class Solution2
{
    public:
        int min_time_multiple_sys(vector<pair<string,int>> &jobs, int m)
        {
            sort(jobs.begin(),jobs.end(),[](pair<string,int> &a, pair<string,int> &b)
            {
                return a.second <= b.second;
            });

            priority_queue<int,vector<int>,greater<int>> servers;

            for (int i=0;i<m;i++)
                servers.push(0);

            int total_time = 0;
            for(auto job: jobs)
            {
                int earliest_server = servers.top();
                servers.pop(); // return type is void unlike that in python

                int new_time = earliest_server + job.second;
                servers.push(new_time);
                total_time += new_time;
            }

            return total_time;
        }
};

int main()
{
    vector<pair<string, int>> jobs = {{"j1", 3}, {"j2", 1}, {"j3", 2}, {"j4", 5}};
    Solution2 sol2;
    cout << sol2.min_time_multiple_sys(jobs, 2) << endl;

    Solution1 sol1;
    cout << sol1.min_time_single_sys(jobs) << endl;
    return 0;
}