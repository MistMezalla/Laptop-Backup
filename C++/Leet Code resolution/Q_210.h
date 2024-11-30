# include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int,vector<int>> adj_list;
        vector<int> in_degrees(0,numCourses);

        int u,v;

        for (v = 0;v < numCourses;v++) {
            adj_list[v] = {};
        }

        for (v = 0; v < numCourses;v++) {
            for (u = 0;u< prerequisites[v].size();u++) {
                adj_list[v].push_back(u);
                in_degrees[v] += 1;
            }
        }

        queue<int> q;
        for (v = 0;v < numCourses;v++) {
            if (in_degrees[v] == 0) {
                q.push(v);
            }
        }

        vector<int> topo_sort;
        while (! q.empty()) {
            int node = q.front();
            q.pop();
            topo_sort.push_back(node);

            for (auto neighbour: adj_list[node]) {
                in_degrees[neighbour] --;
                if (in_degrees[neighbour] == 0)
                    q.push(neighbour);
            }
        }

        return topo_sort.size() == numCourses ? topo_sort : vector<int> {};
    }
};
