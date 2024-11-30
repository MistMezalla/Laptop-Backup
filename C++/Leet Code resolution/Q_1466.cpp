#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minReorder(int n, vector<vector<int>>& connections) {
        unordered_map<int,vector<pair<int,int>>> adj_list;
        vector<int>visited(n,0);
        int cnt = 0;

        // for(u=0;u<n;u++) {
        //     adj_list[u] = {};
        // }

        /*
        -> emplace_back:-
            -> makes in place pair obj
        -> in case of push_back you have to make use of "make_pair" function.
        */

        for (const auto& edge : connections) {
            int u = edge[0], v = edge[1];
            adj_list[u].emplace_back(v, 1);
            adj_list[v].push_back(make_pair(u, 0));
        }

        /*
        -> For nested functions in cpp use the signature given below
        */
        function<void(int)> dfs = [&](int node){
            visited[node] = 1;

            for (auto &[neighbour,sign]: adj_list[node]) {
                if (! visited[neighbour]) {
                    cnt += sign;
                    dfs(neighbour);
                }
            }
        };

        dfs(0);
        return cnt;
    }
};