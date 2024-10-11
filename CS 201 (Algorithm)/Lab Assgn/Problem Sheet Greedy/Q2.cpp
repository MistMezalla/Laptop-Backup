#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        int weighted_job_scheduling(vector<pair<int,int>> &jobs)
        {
            sort(jobs.begin(),jobs.end(),[](pair<int,int> &a,pair<int,int> &b)
            {
                return a.second / a.first >= b.second/ b.first;
            });

            int total_time = 0;
            int curr_time = 0;
            
            for(auto job: jobs)
            {
                curr_time += job.first;
                total_time += job.second * curr_time;
            }
            return total_time;
        }

};

int main()
{
    Solution sol;
    vector<pair<int,int>> jobs=  {{3, 10}, {1, 5}, {2, 7}, {4, 2}};
    cout << sol.weighted_job_scheduling(jobs) << endl;

    // Test case 1: No jobs
    vector<pair<int,int>> jobs1 = {};
    cout << "Test Case 1 (No Jobs): " << sol.weighted_job_scheduling(jobs1) << endl;

    // Test case 2: Single job
    vector<pair<int,int>> jobs2 = {{5, 10}};
    cout << "Test Case 2 (Single Job): " << sol.weighted_job_scheduling(jobs2) << endl;

    // Test case 3: Jobs with zero weight
    vector<pair<int,int>> jobs3 = {{3, 0}, {2, 0}, {4, 0}};
    cout << "Test Case 3 (Jobs with Zero Weight): " << sol.weighted_job_scheduling(jobs3) << endl;

    // // Test case 4: Jobs with zero time
    // vector<pair<int,int>> jobs4 = {{0, 10}, {0, 5}, {0, 7}};
    // cout << "Test Case 4 (Jobs with Zero Time): " << sol.weighted_job_scheduling(jobs4) << endl;

    // Test case 5: All jobs have the same time and weight
    vector<pair<int,int>> jobs5 = {{3, 10}, {3, 10}, {3, 10}};
    cout << "Test Case 5 (Same Time and Weight): " << sol.weighted_job_scheduling(jobs5) << endl;

    // Test case 6: Large weights and times // Overflow due to i/p values
    vector<pair<int,int>> jobs6 = {{1000000, 5000000}, {2000000, 3000000}, {1500000, 4000000}};
    cout << "Test Case 6 (Large Weights and Times): " << sol.weighted_job_scheduling(jobs6) << endl;

    return 0;
}