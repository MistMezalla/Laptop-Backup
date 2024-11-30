#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int, vector<int>> adj_list;
        vector<int> in_degrees(numCourses, 0);  // Correct initialization

        // Build the graph and calculate in-degrees
        for (const auto& prereq : prerequisites) {
            int u = prereq[1];  // u is the prerequisite course
            int v = prereq[0];  // v is the course that depends on u
            adj_list[u].push_back(v);  // Add v to the adjacency list of u
            in_degrees[v] += 1;  // Increment the in-degree of v
        }

        queue<int> q;
        // Push all nodes with in-degree 0 to the queue
        for (int v = 0; v < numCourses; v++) {
            if (in_degrees[v] == 0) {
                q.push(v);
            }
        }

        vector<int> topo_sort;
        // Perform Kahn's Algorithm for topological sorting
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            topo_sort.push_back(node);

            // Reduce the in-degree of all neighbors
            for (auto neighbour : adj_list[node]) {
                in_degrees[neighbour]--;
                if (in_degrees[neighbour] == 0) {
                    q.push(neighbour);
                }
            }
        }

        // Return the result if all courses were taken, otherwise an empty vector
        return topo_sort.size() == numCourses ? topo_sort : vector<int>{};
    }
};



int main() {
    Solution sol;
    vector<vector<int>> pre1 = {{1, 0}, {2, 0}, {3, 1}, {3, 2}};

    vector<int> result = sol.findOrder(4, pre1);

    // Print the result
    for (int course : result) {
        cout << course << " ";
    }
    cout << endl;

    return 0;
}
